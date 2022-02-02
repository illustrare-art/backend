from django.db import models, transaction
from users.models import User
from uuid import uuid4
from django.utils import timezone


class Photo(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4)
    photo_url = models.URLField(null=False, blank=False)
    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="photos"
    )
    post_date = models.DateTimeField()
    post_name = models.CharField(max_length=60)
    description = models.CharField(max_length=400)

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.post_date = timezone.now()
        super().save(*args, **kwargs)


class Bid(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4)
    bid_price = models.FloatField()
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE, related_name="bids")
