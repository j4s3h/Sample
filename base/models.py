from django.db import models
class Task (models.Model):
    name = models.CharField(max_length=50, unique  = True)
    is_complete = models.BooleanField(default=False)
    due_date = models.DateField()
    description = models.TextField()
    board = models.ForeignKey('Board', on_delete=models.CASCADE, related_name='tasks')
class Category(models.Model):
    name = models.CharField(max_length=50, unique  = True)

    def __str__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='boards')
    description = models.TextField()

    def __str__(self):
        return self.name

