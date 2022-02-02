from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from api.mixins import ApiErrorsMixin, ApiAuthMixin, PublicApiMixin

from auth.services import jwt_login, google_validate_id_token
from users.serializers import UserSerializer

from users.services import user_get_or_create


class UserInitView(PublicApiMixin, ApiErrorsMixin, APIView):
    def post(self, request, *args, **kwargs):
        id_token = request.headers.get("Authorization")
        google_validate_id_token(id_token=id_token)

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, _ = user_get_or_create(**serializer.validated_data)

        response = Response(data=serializer.validated_data)
        response = jwt_login(response=response, user=user)

        return response
