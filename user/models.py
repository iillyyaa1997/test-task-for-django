from django.contrib.auth.models import AbstractUser
from django.db import models

from department.models import Department


class User(AbstractUser):
    class Role(models.IntegerChoices):
        USER = 0,
        ADMIN = 1,

    role = models.IntegerField(
        choices=Role.choices,
        default=Role.USER
    )
    username = models.CharField(max_length=150)
    patronymic = models.CharField(
        max_length=256
    )
    login = models.CharField(
        max_length=256,
        unique=True
    )
    photo = models.ImageField(
        null=True
    )
    departament = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='departments',
    )

    USERNAME_FIELD = 'login'
