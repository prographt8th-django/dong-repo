from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from applications.base.models import BaseModel


# Create your models here.
class University(BaseModel):
    """
    대학교 Model 입니다.
    """
    LOCATION_CHOICES = (
        (1, "서울"),
        (2, "경기"),
        (3, "인천"),
        (4, "충청북도"),
        (5, "충청남도"),
        (6, "경상북도"),
        (7, "경상남도"),
        (8, "전라북도"),
        (9, "전라남도"),
        (10, "강원도"),
    )
    name = models.CharField(max_length=30, verbose_name="대학교 이름")
    location = models.IntegerField(choices=LOCATION_CHOICES, verbose_name="대학 소재지")

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    """
    유저를 생성하기 위한 헬퍼 클래스입니다.
    """
    def create_user(self, email, account_id, password, mdn, name):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            account_id=account_id,
            mdn=mdn,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, account_id, password, mdn, name):
        user = self.create_user(
            email,
            password=password,
            account_id=account_id,
            mdn=mdn,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseModel):
    """
    실제 User Model 입니다.
    """
    university = models.ForeignKey(University, null=True, on_delete=models.CASCADE, related_name="user", verbose_name="소속 학교")
    student_id = models.CharField(max_length=15, verbose_name="학번")
    account_id = models.CharField(max_length=20, unique=True, verbose_name="아이디")
    password = models.CharField(max_length=128, verbose_name="패스워드")
    name = models.CharField(max_length=20, verbose_name="이름")
    mdn = models.CharField(max_length=20, verbose_name="전화번호")
    email = models.EmailField(max_length=50, verbose_name="이메일")
    nickname = models.CharField(max_length=20, verbose_name="닉네임")
    is_admin = models.BooleanField(default=False, verbose_name="관리자 권한")
    is_active = models.BooleanField(default=False, verbose_name="계정 활성화 여부")

    objects = UserManager()
    USERNAME_FIELD = 'account_id'
    REQUIRED_FIELDS = ["name", "email", "mdn"]

    def __str__(self):
        return self.name

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
