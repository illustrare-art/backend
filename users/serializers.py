from rest_framework import status, serializers


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False, default="")
    last_name = serializers.CharField(required=False, default="")
