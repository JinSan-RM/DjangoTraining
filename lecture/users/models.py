from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Member(AbstractUser):
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    