from rest_framework import serializers

from core.models import Post, Content


class CreateContentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Content
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'url', 'name']


class PostDetailsSerializer(serializers.ModelSerializer):
    content = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created']

