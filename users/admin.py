from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserSdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields":("role",)}),
    )
