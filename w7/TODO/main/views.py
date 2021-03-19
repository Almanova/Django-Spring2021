from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import TodoList, Task
from .serializers import TodoListSerializer, TodoListDetailSerializer, TaskSerializer


class TodoListViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'completed']:
            return TodoListDetailSerializer
        return self.serializer_class

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.action == 'completed':
            context['is_completed'] = True
        return context

    @action(methods=['get'], detail=True, url_path='completed')
    def completed(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == self.request.user:
            serializer = self.get_serializer(instance=instance,
                                             data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response({"details": "forbidden"})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == self.request.user:
            self.perform_destroy(instance)
            return Response({"details": "deleted"})
        return Response({"details": "forbidden"})
