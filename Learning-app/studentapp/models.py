from django.db import models

# Create your models here.

class Sturesponse(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=50)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=10)
    contactno=models.IntegerField()
    emailaddress=models.CharField(max_length=50)
    responsetype=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    responsetext=models.CharField(max_length=500)
    responsedate=models.CharField(max_length=50)

class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    question=models.TextField()
    postedby=models.CharField(max_length=50)
    posteddate=models.CharField(max_length=50)

class Answer(models.Model):
    aid=models.AutoField(primary_key=True)
    answer=models.TextField()
    answeredby=models.CharField(max_length=50)
    posteddate=models.CharField(max_length=50)
    qid=models.IntegerField()
