from django.urls import path

from . import views


app_name='articles'
urlpatterns = [
    path('', views.article_list, name='list'),
    path('article_create/', views.article_create, name='create'),
    path('article_drafts/', views.article_drafts, name='drafts'),
    path('article_edit/<int:pk>', views.article_edit, name='edit'),
    path('article_detail/<slug:slug>/<int:pk>', views.article_details, name='details'),
    path('article_like/<int:article_id>', views.like, name='like'),
    path('article_search/', views.article_search, name='search'),
    path('delete/<int:pk>', views.article_delete, name='delete'),
]
