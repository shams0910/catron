from django.contrib import admin
from .models import Article
from .models import Like
from .models import Category

# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
