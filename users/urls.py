from django.urls import path

from users.views import UserInitView


urlpatterns = [
    path("init/", UserInitView.as_view(), name="init"),
]
