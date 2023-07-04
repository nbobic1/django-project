from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from core.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        print('validate', data)
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match!", code='passwords_dont_match')
        return data

    def create(self, validated_data):
        print('omggggg', validated_data)
        user = User.objects.create(email=validated_data.get('email'), bio=validated_data.get('bio'))
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'confirm_password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
