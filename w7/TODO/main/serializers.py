from rest_framework import serializers
from .models import TodoList, Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = '__all__'


class TodoListDetailSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'tasks')

    def get_tasks(self, instance):
        is_completed = self.context.get('is_completed', False)
        return TaskSerializer(instance.tasks.filter(
            is_completed=is_completed), many=True).data
