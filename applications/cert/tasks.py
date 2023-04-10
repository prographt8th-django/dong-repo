from django.core.mail import EmailMessage

from config.celery import app


@app.task()
def task_send_email(email, token):
    print("안녕하세요 메일 보내려고 진행중입니다.")
    subject = "오댕 회원가입 테스트입니다."
    # to = [email]
    to = ["odh0112@naver.com"]
    from_email = "odh0112@naver.com"
    message = f"""
    반가워요~ {email.split('@')[0]} 님
    
    로그인을 진행하시고 싶으시다면, 아래의 링크를 복사해 새 탭에 붙여 넣으세요.
    http://127.0.0.1:8000/confirm?token={token}
    """
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
    print("메일 다 보냈습니다.")
