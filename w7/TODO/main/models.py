from django.conf import settings
from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Todo list name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo lists'


class Task(models.Model):
    todo_list = models.ForeignKey(TodoList,
                                  on_delete=models.CASCADE,
                                  related_name='tasks',
                                  verbose_name='Todo list')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='tasks',
                              verbose_name='Owner')
    name = models.CharField(max_length=256,
                            verbose_name='Task name')
    is_completed = models.BooleanField(default=False,
                                       verbose_name='Completed')
    due_on = models.DateTimeField(blank=True,
                                  null=True,
                                  verbose_name='Due on')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['due_on']
