from django.contrib import admin

# Register your models here.
from blog.models import Category,Article, ArticleImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent')


class ArticleAdmin(admin.ModelAdmin):
    list_display =  ('title','body','user')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)