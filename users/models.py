from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from roles import models as roles_models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=150, blank=True, verbose_name="Имя")
    city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="Возраст")
    role = models.ForeignKey(
        roles_models.Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name="users",
        verbose_name="Роль"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
