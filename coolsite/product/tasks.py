from coolsite.celery import app
from product.services import send


@app.task
def send_spam_email(user_email):
    send(user_email)
