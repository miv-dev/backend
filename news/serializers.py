from rest_framework import serializers
from .models import News, NewsPhoto

class NewsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPhoto
        fields = ['id', 'image', 'description', 'created_at']

class NewsSerializer(serializers.ModelSerializer):
    photos = NewsPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'created_at', 'updated_at', 'photos']