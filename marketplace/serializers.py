from rest_framework import serializers

from marketplace.models import Photo


class PhotoDetailSerializer(serializers.ModelSerializer):
    photo_url = serializers.URLField()
    user_id = serializers.IntegerField()
    post_name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Photo
        fields = ['username', 'profile_photo', 'phone_number']
