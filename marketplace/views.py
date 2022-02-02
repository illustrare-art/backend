from rest_framework.generics import ListCreateAPIView
from api.mixins import ApiErrorsMixin, ApiAuthMixin
from marketplace.serializers import PhotoDetailSerializer
from marketplace.models import Photo


class PhotoListCreateView(ListCreateAPIView, ApiAuthMixin, ApiErrorsMixin):
    serializer_class = PhotoDetailSerializer
    queryset = Photo.objects.all()
