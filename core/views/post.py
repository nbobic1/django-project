from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.serializers import PostDetailsSerializer, PostInfoSerializer, CreateContentSerializer, PostCreateSerializer, \
    ContentSerializer
from core.models import Post, Content
from core.utils.pagination import HundredSetPagination


class PostsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostInfoSerializer
    pagination_class = HundredSetPagination
    queryset = Post.objects.filter(published=True)


class PostView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailsSerializer

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        return Response(PostDetailsSerializer(post).data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        content_ids = serializer.validated_data.pop('content_ids', [])

        post = Post.objects.create(**serializer.validated_data, user=request.user, published=True)
        Content.objects.filter(id__in=content_ids).update(post=post)
        return Response(PostDetailsSerializer(post).data, status=status.HTTP_201_CREATED)

    def put(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if not post.user:
            raise Exception("Can not update post")

        serializer = PostDetailsSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        Post.objects.filter(id=post_id).update(**serializer.validated_data)
        return Response(PostDetailsSerializer(post).data, status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        if not Post.objects.get(id=post_id).user:
            raise Exception("Can not delete post")
        Post.objects.filter(id=post_id).delete()
        return Response(status=status.HTTP_200_OK)


class ContentView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailsSerializer

    def post(self, request):
        serializer = CreateContentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        content = Content.objects.create(**serializer.validated_data)
        return Response(ContentSerializer(content).data, status=status.HTTP_201_CREATED)

    def update(self, request, content_id):
        if not Content.objects.filter(id=content_id).post.user:
            raise Exception("Can not update post")

        serializer = CreateContentSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        content = Content.objects.filter(id=content_id).update(**serializer.validated_data)
        return Response(ContentSerializer(content.post).data, status=status.HTTP_200_OK)

    def delete(self, request, content_id):
        content = Content.objects.get(id=content_id)
        if content.post and not content.post.user:
            raise Exception("Can not delete content")
        Content.objects.filter(id=content_id).delete()
        return Response(status=status.HTTP_200_OK)

