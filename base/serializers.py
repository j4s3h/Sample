from rest_framework import serializers
from .models import Category, Board, Task


class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Category
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset = Category.objects.all()) 
    class Meta:
        model = Board
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    board = serializers.SlugRelatedField(slug_field='name', queryset = Board.objects.all()) 
    class Meta:
        model = Task
        fields = '__all__'
        