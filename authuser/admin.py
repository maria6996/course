from django.contrib import admin
from authuser.models import User, Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price','user')

admin.site.register(User)
admin.site.register(Course, CourseAdmin)
