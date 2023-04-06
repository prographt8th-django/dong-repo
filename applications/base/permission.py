from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Admin인지 체크하는 인증 로직입니다.
    """
    message = {'message': 'CERTIFICATION_FAILURE'}

    def has_permission(self, request, view):
        if request.user and request.user.is_admin:
            raise AuthenticationFailed(detail=self.message)
