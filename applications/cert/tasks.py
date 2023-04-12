from django.core.mail import EmailMessage

from config.celery import app


@app.task()
def task_send_email(email, token):
    print("========= send email start =========")
    subject = "오댕 회원가입 테스트입니다."
    to = [email]
    from_email = "odh0112@naver.com"
    message = f"""
    반가워요~ {email.split('@')[0]} 님

    로그인을 진행하시고 싶으시다면, 아래의 링크를 복사해 새 탭에 붙여 넣으세요.
    아래의 링크는 10분간 유효합니다.
    http://127.0.0.1:8000/v1/cert/user/confirm?token={token}
    """
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
    print("========= send email end =========")
