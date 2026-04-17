from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 'id' automatic banta hai, password 'write_only' hai security ke liye
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data.get('name', ''),
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """
        Password update ko handle karne ke liye security fix.
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance