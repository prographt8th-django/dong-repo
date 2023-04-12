from django.utils.crypto import get_random_string


def randomToken():
    """
    이메일 인증 시 임시 토큰 생성 함수입니다.
    """
    return get_random_string(length=50)
