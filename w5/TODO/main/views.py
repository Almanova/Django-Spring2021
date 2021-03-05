from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import TodoList
from .serializers import TodoListSerializer


class Todos(generics.GenericAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'todo_list': serializer.data})


class CompletedTodos(Todos):
    template_name = 'completed_todo_list.html'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['is_completed'] = True
        return context
