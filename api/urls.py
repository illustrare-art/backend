from django.urls import path, include


urlpatterns = [
    path("auth/", include(("auth.urls", "auth"))),
    path("users/", include(("users.urls", "users"))),
]
