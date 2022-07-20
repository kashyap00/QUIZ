from django.db import models

# Create your models here.

class Candidate(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address1=models.CharField(max_length=122)
    address2=models.CharField(max_length=122)
    city=models.CharField(max_length=22)
    state=models.CharField(max_length=22)
    zip=models.CharField(max_length=22)
    date=models.DateField()
    def __str__(self):
        return self.email

class Questionmaker(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address1=models.CharField(max_length=122)
    address2=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    state=models.CharField(max_length=22)
    zipc=models.CharField(max_length=22) 
    date=models.DateField() 
    def __str__(self):
        return self.email






