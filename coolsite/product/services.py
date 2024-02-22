from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'В магазине много новинок!',
        'Ждем вас на этой неделе',
        'sushiclubmaster@gmail.com',
        [user_email],
        fail_silently=False
    )
