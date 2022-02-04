from rest_framework import status
from rest_framework.views import APIView

from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse,JsonResponse

from api.mixins import ApiErrorsMixin, PublicApiMixin, ApiAuthMixin
from auth.serializers import GoogleLoginSerializer

from users.services import user_change_secret_key, user_get_or_create

from auth.services import jwt_login, google_get_access_token, google_get_user_info


class GoogleLoginView(PublicApiMixin, ApiErrorsMixin, APIView):
    serializer_class = GoogleLoginSerializer

    def handle_access_token(self,access_token):
        user_data = google_get_user_info(access_token=access_token)

        profile_data = {
            "email": user_data["email"],
            "first_name": user_data.get("given_name", ""),
            "last_name": user_data.get("family_name", ""),
        }
        user, _ = user_get_or_create(**profile_data)

        response = JsonResponse(
            {"success": True},
        )
        response = jwt_login(response=response, user=user)
        return response

    def get(self, request, *args, **kwargs):
        input_serializer = self.serializer_class(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data
        code = validated_data.get("code")
        error = validated_data.get("error")
        access_token = validated_data.get("access_token")
        print(validated_data)
        if access_token:
            return self.handle_access_token(access_token)

        if error or not code:
            return HttpResponse(
                {"success": False},
                status=status.HTTP_401_UNAUTHORIZED,
                content_type="application/json",
            )

        domain = settings.BASE_BACKEND_URL
        api_uri = reverse("api:auth:login-with-google")
        redirect_uri = f"{domain}{api_uri}"

        access_token = google_get_access_token(code=code, redirect_uri=redirect_uri)
        return self.handle_access_token(access_token)



class LogoutView(ApiAuthMixin, ApiErrorsMixin, APIView):
    def post(self, request):
        """
        Logs out user by removing JWT cookie header.
        """
        user_change_secret_key(user=request.user)

        response = HttpResponse(status=status.HTTP_202_ACCEPTED)
        response.delete_cookie(settings.JWT_AUTH["JWT_AUTH_COOKIE"])
        return response
