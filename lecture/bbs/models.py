from django.db import models

# Create your models here.
class Board(models.Model):
    
    #b_no = models.IntegerField(primary_key=True)
    b_title = models.CharField(max_length=100)
    b_author = models.CharField(max_length=20)
    b_content = models.CharField(max_length=500)
    b_date = models.DateTimeField(auto_now_add=True)
    b_comment_count = models.IntegerField(default=0)
    b_like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.b_title

class Comment(models.Model):
    c_author = models.CharField(max_length=20)
    c_content = models.CharField(max_length=500)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)

    def __str__(self):
        return self.c_content
