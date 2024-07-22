from rest_framework import serializers

from .models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    cat_name = serializers.CharField(source='cat.name')
    cat_id = serializers.CharField(source='cat.id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'date_creation', 'text', 'cat_name', 'cat_id', 'preview', 'image',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
