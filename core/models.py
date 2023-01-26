from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

class User(AbstractUser):
    UNKNOWN = "unknown"
    USER= "user"
    ADMINISTRATOR = "administrator"
    ROLE = [(UNKNOWN, "unknown"), (USER, "user"), (ADMINISTRATOR, "administrator")]

    role = models.CharField(max_length=14, choices=ROLE, default=UNKNOWN)
    age = models.IntegerField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
