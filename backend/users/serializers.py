from rest_framework import serializers
from .models import User  # Ensure path is correct for your 'users' app

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def create(self, validated_data):
    #     # Hum direct naya UserManager use kar rahe hain
    #     return User.objects.create_user(
    #         email=validated_data['email'],
    #         name=validated_data.get('name', ''),
    #         password=validated_data['password']
    #     )