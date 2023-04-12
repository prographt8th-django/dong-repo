from rest_framework import serializers

from applications.board.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField()
    scrap_count = serializers.IntegerField()

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
