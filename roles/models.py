from django.db import models


class Role(models.Model):
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name="Название роли",
    )

    def __str__(self):
        return self.title
