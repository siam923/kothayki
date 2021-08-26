from rest_framework import serializers
from .models import CustomUser
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer


class LoginSerializer(RestAuthLoginSerializer):
    username = None


class UserSerializer(serializers.ModelSerializer):
    """
    ``Serializer`` for ``User`` ..
    """

    class Meta:
        model = CustomUser
        fields = ('id', 'avatar', 'username', 'email', 'first_name', 'last_name',
                  'password', 'is_active', 'is_staff', 'is_youtuber',
                  'is_owner',)
        read_only_fields = ('is_active', 'is_staff', 'is_owner')
        extra_kwargs = {
            'password': {'write_only': True}
        }
