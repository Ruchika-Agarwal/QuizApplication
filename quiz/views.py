from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req,'base.html')

def select_category(req):
    return render(req,'select_category.html')

def textall_categories(req):
    catdata=models.Question_Set.objects.all()
    return render(req,"textall_cat.html",{'data':catdata})

def imgall_categories(req):
    catdata=models.Question_Set.objects.all()
    return render(req,"imgall_cat.html",{'data':catdata})


def textcategory_questions(req,cat_id):

    #question=models.Question.objects.get(id=que_id)
    #category=models.Question_Set.objects.filter(questions=question)
    
    category=models.Question_Set.objects.get(id=cat_id)
    question=models.Question.objects.filter(question_set=category).order_by('id').all()
    
    
    #op=models.Question.objects.values('options')
    #opt=models.Options.objects.filter(option=op)
    #category = models.Question_Set.objects.get(id=cat_id)
    #question = category.choices.all()
   
    
    print(category)
    print(question)
    
    return render(req,"textcategory_questions.html",{'category':category,'question':question})


def imgcategory_questions(req,cat_id):
    category=models.Question_Set.objects.get(id=cat_id)
    question=models.Question.objects.filter(question_set=category).order_by('id').all()
    print(category)
    print(question)
    return render(req,"imgcategory_questions.html",{'category':category,'question':question})