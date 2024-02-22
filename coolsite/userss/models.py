from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=156, unique=True, verbose_name='Ник')
    image = models.ImageField(upload_to='users_images', verbose_name='Аватар')
    address = models.CharField(max_length=156, verbose_name='Адрес доставки')
