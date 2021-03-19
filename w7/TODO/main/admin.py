from django.contrib import admin
from .models import TodoList, Task


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'todo_list', 'name', 'created_at', 'due_on', 'owner', 'is_completed')
    list_filter = ('todo_list', 'created_at', 'due_on', 'owner', 'is_completed')
    search_fields = ('name', 'owner__username', 'todo_list__name')
