from django.db import models

class ToDoList(models.Model):
    todo_text = models.CharField(max_length = 40)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.todo_text)
