from rest_framework import viewsets
from rest_framework.response import Response

from applications.base.permission import IsAdminUser
from applications.base.response import operation_success
from applications.cert.models import University, User
from applications.cert.serializers import UniversitySerializer, UserSerializer, UserDetailSerializer
from django.core.cache import cache

from applications.cert.tasks import task_send_email


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

    def create(self, requset, *args, **kwargs):
        # TODO: 회원가입을 하면 token : id 로 캐쉬에 저장하고
        # TODO: 이메일로 celery 이용해 보내고
        # TODO: account로 보내서 검증 후 is_active 활성화
        try:
            task_send_email.delay("odh0112@naver.com", "asdsadasd")
        except Exception as e:
            print(e)

        return Response("aaa")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.detail_serializer_class(instance)
        return Response(serializer.data)

    # def certify(self, request):
    #     cache.