from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.admin.serializers import PostDetailsSerializer, PostInfoSerializer, CreateContentSerializer
from core.models import Post, Content
from core.utils.pagination import HundredSetPagination


class AdminPostCreateListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostInfoSerializer
    pagination_class = HundredSetPagination
    queryset = Post.objects.all()


class AdminPostView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailsSerializer

    def post(self, request):
        serializer = PostDetailsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post = Post.objects.create(**serializer.validated_data)
        return Response(PostDetailsSerializer(post).data, status=status.HTTP_201_CREATED)

    def update(self, request, post_id):
        serializer = PostDetailsSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        post = Post.objects.filter(id=post_id).update(**serializer.validated_data)
        return Response(PostDetailsSerializer(post).data, status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        Post.objects.delete(id=post_id)
        return Response(status=status.HTTP_200_OK)


class AdminContentView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailsSerializer

    def post(self, request):
        serializer = CreateContentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        content = Content.objects.create(**serializer.validated_data)
        return Response(PostDetailsSerializer(content.post).data, status=status.HTTP_201_CREATED)

    def update(self, request, content_id):
        serializer = CreateContentSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        content = Content.objects.filter(id=content_id).update(**serializer.validated_data)
        return Response(PostDetailsSerializer(content.post).data, status=status.HTTP_200_OK)

    def delete(self, request, content_id):
        Content.objects.delete(id=content_id)
        return Response(status=status.HTTP_200_OK)

