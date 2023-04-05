from django.db import models

from applications.base.models import BaseModel
from applications.cert.models import User


# Create your models here.

class Notice(BaseModel):
    """
    공지사항 Model 입니다.
    """
    TYPE_CHOICES = [
        (1, '안내'),
        (2, '중요'),
        (3, '점검')
    ]

    title = models.CharField(max_length=255, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    guide_type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='공지 타입')
    user = models.ForeignKey(User, related_name="notice", on_delete=models.SET_NULL, null=True, verbose_name="작성자")

    def __str__(self):
        return self.title


class Post(BaseModel):
    """
    게시물 model 입니다.
    댓글 및 스크랩 개수는 컬럼으로 선언하는 것보다 다른 테이블 개수 산정해 가져오는 방법이 더 좋을거 같음
    """
    user = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(max_length=255, verbose_name="제목")
    contents = models.TextField(verbose_name='내용')
    empathy_count = models.IntegerField(default=0, verbose_name="공감 개수")
    is_anonymous = models.BooleanField(default=True, verbose_name="익명 여부")
    alarm_active = models.BooleanField(default=True, verbose_name="알람 활성화 여부")

    def __str__(self):
        return self.title

    @property
    def comment_count(self):
        if self.id:
            return Comment.objects.filter(post=self.id).count()
        return 0

    @property
    def scrap_count(self):
        if self.id:
            return Scrap.objects.filter(post=self.id).count()
        return 0


class Comment(BaseModel):
    """
    댓글 model 입니다.
    """
    user = models.ForeignKey(User, related_name="comment", on_delete=models.CASCADE, verbose_name="작성자")
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE, verbose_name="게시물")
    contents = models.TextField(verbose_name='내용')
    empathy_count = models.IntegerField(default=0, verbose_name="공감 개수")

    def __str__(self):
        return self.contents


class Scrap(BaseModel):
    """
    댓글 model 입니다.
    """
    user = models.ForeignKey(User, related_name="scrap", on_delete=models.CASCADE, verbose_name="작성자")
    post = models.ForeignKey(Post, related_name="scrap", on_delete=models.CASCADE, verbose_name="게시물")

    def __str__(self):
        return self.title
