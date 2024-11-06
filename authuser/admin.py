from django.contrib import admin
from authuser.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','user_type','mobile','is_active')

admin.site.register(User,UserAdmin)
