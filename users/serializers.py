from rest_framework import serializers
from users.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'city', 'age')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True, 'allow_blank': False},
            'city': {'required': True, 'allow_blank': False},
            'age': {'required': True},
        }
    
    def validate_first_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Поле 'Имя' не может быть пустым")
        return value

    def validate_city(self, value):
        if not value.strip():
            raise serializers.ValidationError("Поле 'Город' не может быть пустым")
        return value

    def validate_age(self, value):
        if value is None:
            raise serializers.ValidationError("Поле 'Возраст' обязательно для заполнения")
        if value < 0:
            raise serializers.ValidationError("Возраст не может быть отрицательным")
        return value
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            city=validated_data.get('city', ''),
            age=validated_data.get('age')
        )
        return user