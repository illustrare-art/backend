from django.urls import path

from users.views import UserInitView, UserUpdateProfileView


urlpatterns = [
    path("init/", UserInitView.as_view(), name="init"),
    path(
        "profile/<uuid:user_uuid>/",
        UserUpdateProfileView.as_view(),
        name="set-profile",
    ),
]
