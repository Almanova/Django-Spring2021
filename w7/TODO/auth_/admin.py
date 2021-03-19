from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at')
    list_filter = ('created_at', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
