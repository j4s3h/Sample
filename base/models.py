from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='boards')
    description = models.TextField()

    def __str__(self):
        return self.name

