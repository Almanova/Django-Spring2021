from rest_framework import routers

from main import views


router = routers.DefaultRouter()
router.register('todos', views.TodoListViewSet, basename='todos')
router.register('tasks', views.TaskViewSet, basename='tasks')


urlpatterns = router.urls
