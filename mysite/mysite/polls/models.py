from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pud_date = models.DateTimeField('Published date')

class Choice(models.Model):
    question =models.ForeignKey(Question,on_delete=models.CASCADE)  
    choice_text = models.CharField(max_length=250) 
    votes = models.IntegerField(default=0)