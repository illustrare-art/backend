from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False, default="")
    last_name = serializers.CharField(required=False, default="")


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    profile_photo = serializers.URLField()
    phone_number = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'profile_photo', 'phone_number']
