import datetime 
from django.db import models
from django.utils import timezone

class Question(models.Model):

    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("published date")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime().timedelta(days=1)

class Choices(models.Model):

    question = models.ForeignKey(Question , on_delete= models.CASCADE)
    choices_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choices_text



