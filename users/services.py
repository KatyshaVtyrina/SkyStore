from django.core.mail import send_mail

from config import settings
from users.models import User


def send_code_email(user: User):
    send_mail(
        'Подтверждение почты',
        f'Чтобы подтвердить почту, перейдите по ссылке http://127.0.0.1:8000/users/verification/{user.id}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )