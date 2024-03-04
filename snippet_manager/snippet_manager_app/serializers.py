from rest_framework import serializers
from .models import Tag, Snippet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['id','username','email','password']

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
        
class SnippetSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    id = serializers.IntegerField(read_only = True)
    timestamp = serializers.DateTimeField(read_only = True)
    user = UserSerializer(read_only = True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'content', 'timestamp', 'user', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        snippet = Snippet.objects.create(**validated_data)
        for tag_data in tags_data:
            snippet.tags.add(tag_data)
        return snippet
    
class DetailAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = [ 'title', 'content', 'timestamp']