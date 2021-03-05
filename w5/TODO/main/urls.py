from django.urls import path
from main import views

urlpatterns = [
    path('<int:pk>/', views.Todos.as_view(), name='todos'),
    path('<int:pk>/completed/', views.CompletedTodos.as_view(), name='completed_todos')
]
