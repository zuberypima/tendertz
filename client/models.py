from django.db import models

# Create your models here.

class ClientDetail(models.Model):
    idNo=models.CharField(max_length=255)
    orgName=models.CharField(max_length=255)
    CATEGORY =[
        ('Private','Private'),
        ('Public','Public'),
        ('Government','Government')
    ]
    orgCategory=models.CharField(max_length=255,choices=CATEGORY)
    def __str__(self):
        return self.orgName
    
    
class CreateCond(models.Model):
    condDetails=models.CharField(max_length=255)
    condValue=models.CharField(max_length=255)
    def __str__(self):
        return self.condDetails