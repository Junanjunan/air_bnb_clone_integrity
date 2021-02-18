from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin """
    
    fieldsets = UserAdmin.fieldsets +(  ("Custom Profile", {"fields": ("avatar", "gender", "bio", "birthdate", "language", "currency", "superhost", 'login_method')}),  )  # tuple, list 형태를 위해 , 마지막에 이상한 모양으로 들어감  

    list_filter = UserAdmin.list_filter + ('superhost',)

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser',
        'email_verified',
        'email_secret',
        'login_method'
    )