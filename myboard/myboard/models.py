from django.db import models

class myboard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()

    def __str__(self):      #myboard의 object(row)를 출력할 때 메모리 출력 대신에 정의된 것이 출력
        mytitle = str({'mytitle':self.mytitle})
        return mytitle


