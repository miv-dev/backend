from rest_framework import serializers
from .models import Event, EventPhoto, Certificate

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'title', 'file', 'created_at']

class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPhoto
        fields = ['id', 'image', 'description', 'created_at']

class EventSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    photos = EventPhotoSerializer(many=True, read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'date', 'location',
            'registration_link', 'achieved_places',
            'status', 'photos', 'certificates',
        ]

    def to_representation(self, instance):
        """
        Изменяем представление в зависимости от статуса мероприятия
        """
        data = super().to_representation(instance)
        if instance.status == 'upcoming':
            # Для предстоящих мероприятий возвращаем только основную информацию
            fields_to_remove = ['photos', 'certificates', 'achieved_places']
            for field in fields_to_remove:
                data.pop(field, None)
        return data