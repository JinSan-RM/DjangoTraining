from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
        # object의 메모리 번지 이름

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE) # Question 질문이 삭제되면 연결된 Foreignkey choice_text들도 자동 삭제

    def __str__(self):
        return self.choice_text