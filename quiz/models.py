from django.db import models

# Create your models here

class Options(models.Model):

    option = models.CharField(max_length=150)
    '''op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)'''

    def __str__(self):
        return self.option

class Question(models.Model):
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    correct_ans = models.CharField(max_length=150)
    explanation = models.TextField(max_length=500)
    options = models.ManyToManyField(Options,blank=True)
    def __str__(self):
        return self.text

class Question_Set(models.Model):
    section = models.CharField(max_length=50)
    questions = models.ManyToManyField(Question,blank=True)

    def __str__(self):
        return self.section