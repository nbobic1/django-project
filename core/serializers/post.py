from rest_framework import serializers

from core.models import Post, Content
from core.utils.constants import CONTENT_TYPE


class CreateContentSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=CONTENT_TYPE)

    class Meta:
        model = Content
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'url', 'type', 'name', 'text']


class PostCreateSerializer(serializers.ModelSerializer):
    content_ids = serializers.ListField(child=serializers.IntegerField(), allow_null=False, allow_empty=False)

    class Meta:
        model = Post
        exclude = ['published']


class PostDetailsSerializer(serializers.ModelSerializer):
    content = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        exclude = ['published']


class PostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created']

