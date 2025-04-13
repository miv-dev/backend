from django.contrib.auth.models import AbstractUser
from django.db import models
from roles import models as roles_models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        roles_models.Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name="users",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
