from django.urls import path
from main import views

urlpatterns = [
    path('', views.Todos.as_view(), name='todos'),
    path('1/completed/', views.CompletedTodos.as_view(), name='completed_todos')
]
