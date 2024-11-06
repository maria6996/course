from django.contrib import admin
from training.models import Course, CourseDetail, Category, CourseImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description')


class CourseImageInline(admin.TabularInline):
    model = CourseImage
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active','price','Category')
    inlines = [CourseImageInline]
    list_display_links = ['title','Category']


class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'order','course')
    list_display_links = ['course']


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseDetail, CourseDetailAdmin)
admin.site.register(Category, CategoryAdmin)
