from django.urls import path, include
from auth.views import GoogleLoginView, LogoutView


login_patterns = [
    path("google/", GoogleLoginView.as_view(), name="login-with-google"),
]

urlpatterns = [
    path("login/", include(login_patterns)),
    path("logout/", LogoutView.as_view(), name="logout"),
]
