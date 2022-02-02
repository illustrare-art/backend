from django.urls import path

from marketplace.views import PhotoListCreateView


urlpatterns = [
    path("photo/", PhotoListCreateView.as_view(), name="add-photo"),
]
