import jdatetime
from django.contrib import admin

# Register your models here.
from blog.models import Category,Article, ArticleImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent')
    list_display_links = ('title',)

#
# def formatted_created_at(obj):
#      return jdatetime.date.fromgregorian(date=obj.created_at).strftime('%Y-%m-%d')


class ArticleAdmin(admin.ModelAdmin):
    list_display =  ('title','short_description','user','formatted_created_at','created_at')

    def formatted_created_at(self, obj):
        return jdatetime.date.fromgregorian(date=obj.created_at).strftime('%Y-%m-%d')

    # formatted_created_at.admin_order_field = 'created_at'  # Allow sorting by created_at
    formatted_created_at.short_description = 'تاریخ ایجاد'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)