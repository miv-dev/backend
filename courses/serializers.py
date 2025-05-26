from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from courses.models import Course, Enrollment


class CourseSerializer(ModelSerializer):

    enrollment_state = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_enrollment_state(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return None  # Если пользователь не аутентифицирован, возвращаем None

        try:
            enrollment = Enrollment.objects.get(user=user, course=obj)
            return enrollment.state
        except Enrollment.DoesNotExist:
            return None