from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from department.models import Department


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.IntegerChoices):
        USER = 0,
        ADMIN = 1,

    role = models.IntegerField(
        choices=Role.choices,
        default=Role.USER
    )
    last_name = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
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
        related_name='users',
    )

    USERNAME_FIELD = 'login'
