from rest_framework import serializers
from .models import TodoList, Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y')
    due_on = serializers.DateTimeField(format='%d/%m/%Y')
    owner = serializers.CharField(source='owner.username')

    class Meta:
        model = Task
        fields = ('name', 'created_at', 'due_on', 'owner', 'is_completed')


class TodoListSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = TodoList
        fields = ('name', 'tasks')

    def get_tasks(self, instance):
        is_completed = self.context.get('is_completed', False)
        return TaskSerializer(instance.tasks.filter(
            is_completed=is_completed), many=True).data
