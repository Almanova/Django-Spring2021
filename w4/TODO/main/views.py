from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from utils.json_tool import read_json


class Todos(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'
    todos = read_json('static/mock/todos.json')

    def get(self, request):
        return Response({'todos': self.todos})


class CompletedTodos(Todos):
    template_name = 'completed_todo_list.html'
