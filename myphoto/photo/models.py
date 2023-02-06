from django.db import models

# Create your models here.

class photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.title)
