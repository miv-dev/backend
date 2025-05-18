from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата и время")
    location = models.CharField(max_length=255, verbose_name="Место проведения")
    registration_link = models.URLField(verbose_name="Ссылка на регистрацию", blank=True)
    achieved_places = models.TextField(verbose_name="Занятые места", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['-date']

    @property
    def status(self):
        """Определяет статус мероприятия: предстоящее или завершенное"""
        if not self.date:
            return "upcoming"
        return "finished" if self.date < timezone.now() else "upcoming"

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='events/photos/', verbose_name="Фотография")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фотография мероприятия"
        verbose_name_plural = "Фотографии мероприятий"

class Certificate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=255, verbose_name="Название")
    file = models.FileField(upload_to='events/certificates/', verbose_name="Файл")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сертификат/Диплом"
        verbose_name_plural = "Сертификаты/Дипломы"
