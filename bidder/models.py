from django.db import models

# Create your models here.
# Create models for tbidder to be registerend 
class BidderReg(models.Model):
    companyName=models.CharField(max_length=255)
    tinNo=models.CharField(max_length=255)
    companyRegNo =models.CharField(max_length=255)
    vatNo=models.CharField(max_length=255)
    location =models.CharField(max_length=255)
    region=models.CharField(max_length=255)
    dictrict=models.CharField(max_length=255)
    phone =models.CharField(max_length=255)
    email =models.EmailField()
    website =models.CharField(max_length=255)
    business=models.CharField(max_length=255)
    category =models.CharField(max_length=255)
    foreignInput =models.CharField(max_length=255)
    employeeNum =models.CharField(max_length=255)
    def __str__(self):
        return self.companyName