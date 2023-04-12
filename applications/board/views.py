from rest_framework import viewsets

from applications.board.models import Post, Comment
from applications.board.serializers import PostSerializer, CommentSerializer


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
