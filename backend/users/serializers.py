from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 'id' automatic banta hai, password 'write_only' hai security ke liye
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': False, 'allow_null': True}
        }

    def create(self, validated_data):
        # validated_data.pop('username', None) 
        return User.objects.create_user(**validated_data)

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
    

