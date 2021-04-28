from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
import time


from asgiref.sync import sync_to_async
#models
from .models import Article
from .models import Category
from .models import Like



# Create your views here.

def article_list(request):
    articles = Article.objects.filter(published_at__isnull=False).order_by('created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_search(request):
    search_query = request.GET['search']
    results = Article.objects.filter(title__contains=search_query)
    return render(request, 'articles/article_list.html', {'articles': results})


@login_required()
def article_drafts(request):
    drafts = Article.objects.filter(published_at__isnull=True)
    return render(request, 'articles/article_list.html', {'articles': drafts})


def save_instance(title):
    instance = Category(title=title)
    instance.save()
    return instance

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user


            print(instance)
            saved_new_cats = []
            

            if 'save_draft' in request.POST: 
                instance.save()

            elif 'publish_now' in request.POST:
                print(request.POST)
                instance.publish()

            else:
                return HttpResponse('Something went wrong')
              

            if request.POST.get('category', False):
                instance.category.add(request.POST['category'])


            if 'new-category' in request.POST:
                # new_categories = [Category(title=cat) for cat in request.POST.getlist('new-category')]
                print(request.POST.getlist('new-category')) 
                
                for cat in request.POST.getlist('new-category'):
                    saved = sync_to_async(save_instance(cat), thread_sensitive=True)
                    print(saved.id, "this")
                    instance.category.add(saved.id)
            # if len(saved_new_cats)!=0:
            #     print("Performing adding new categories")
            #     for c in saved_new_cats: print('Prining ids', c.id)
            # else:
            #     print("Sorry")
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

    

@login_required(login_url="/accounts/login/")
def article_edit(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            form = forms.CreateArticle(request.POST, request.FILES, instance=article)
            form.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle(instance=article)
    return render(request, 'articles/article_edit.html', {'form': form})

@login_required(login_url="/accounts/login/")
def article_delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:list')
    else:
        return redirect('articles:list')


@login_required(login_url="/accounts/login/")
def article_details(request, slug, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/article_details.html', {'article': article})

@login_required()
def like(request, article_id):
    new_like, created = Like.objects.get_or_create(user=request.user, article_id=article_id)
    if not created:
        new_like.delete()
    return redirect('articles:list')
