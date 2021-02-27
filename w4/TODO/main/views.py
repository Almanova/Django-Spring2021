from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from utils.json_tool import read_json


class Todos(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'

    def get(self, request):
        todos = read_json('static/mock/todos.json')
        return Response({'todos': todos})


class CompletedTodos(Todos):
    template_name = 'completed_todo_list.html'
