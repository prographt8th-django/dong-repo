from rest_framework import viewsets
from rest_framework.response import Response

from applications.base.permission import IsAdminUser
from rest_framework.decorators import action
from applications.base.response import operation_success, operation_failure
from applications.cert.models import University, User
from applications.cert.serializers import UniversitySerializer, UserSerializer, UserDetailSerializer
from django.core.cache import cache

from applications.cert.tasks import task_send_email
from applications.cert.utils import randomToken
from config.settings import CACHE_TTL_DEFAULT


# Create your views here.

class UniversityViewSet(viewsets.ModelViewSet):
    """
    대학교 CRUD API입니다.
    """
    # TODO : 관리자만 CRUD 할 수 있도록 수정 필요
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    # permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return operation_success


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                token = randomToken()
                cache.set(token, user.email, CACHE_TTL_DEFAULT)
                task_send_email.delay(user.email, token)
            else:
                return operation_failure
        except Exception as e:
            return operation_failure

        return Response(self.serializer_class(user).data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.detail_serializer_class(instance)
        return Response(serializer.data)
