from django.db import models

# Create your models here.


class TenderReg(models.Model):
    regNo = models.CharField(max_length=255)
    description = models.TextField()
    clinteId = models.CharField(max_length=255, blank=True, null=True)
    deadLineDate = models.DateField()
    procure_method = models.CharField(max_length=255)
    STATU_TYPE =[
        ('Evaluated','Evaluated'),
        ('Bid Submission','Bid Submission'),
        ('Awarded','Awarded'),
        ('Canceled','Canceled')
    ]
    tender_status = models.CharField(max_length=255,choices=STATU_TYPE)
    financial_value = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.regNo
