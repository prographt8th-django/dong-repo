from django.db import models


class BaseModel(models.Model):
    """
    created_at, updated_at로 구성된 기본 Base Model입니다.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")

    class Meta:
        abstract = True
