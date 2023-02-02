from django.db import models

class Myboard(models.Model):    # myboard : table이 될 것입니다.
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()

# myboard table
# 컬럼명 : myname, mytitle, mycontent, mydate

    def __str__(self):
        return str({'myname':self.myname})