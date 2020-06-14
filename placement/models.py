from django.db import models

# Create your models here.


class CompanyDatabase(models.Model):
    name = models.CharField(max_length=30)
    ctc = models.FloatField(default = 0)
    base = models.FloatField(default = 0)
    #date_of_visit = models.DateField(default = None)
    cgpa = models.FloatField(default=0)
    total_offers = models.IntegerField(default = 0)
    open_dream = models.BooleanField(default = False)
    year = models.FloatField(default = 2020)

class PresentYear(models.Model):
    year = models.IntegerField(default = 2020)
