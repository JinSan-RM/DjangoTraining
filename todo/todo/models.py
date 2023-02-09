from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    imagefile = models.ImageField(upload_to = settings.MEDIA_ROOT, blank=True, null=True)

    def __str__(self):
        return self.title