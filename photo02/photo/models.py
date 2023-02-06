from django.db import models

from django.conf import settings

class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    imagefile = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True) 
    # upload_to는   이미지를 어디에 저장할 거니?
    # blank=True, null=True 비여있는 것 허용, 값 없는 것 허용
    description = models.TextField()
    price = models.IntegerField()
    # upload = models.FileField()
    # upload_path = models.FilePathField()
