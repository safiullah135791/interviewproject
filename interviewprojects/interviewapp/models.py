from django.db import models
# Create your models here.
class Datas(models.Model):
    morning10 = models.IntegerField(default='')
    afternoon2 = models.IntegerField(default='')
    evening6 = models.IntegerField(default='')
    night10 = models.IntegerField(default='')
    firsttotal = models.IntegerField(default='')
    firstrupess10 = models.IntegerField(default='')
    rupess2 = models.IntegerField(default='')
    rupess6 = models.IntegerField(default='')
    lastrupess10 = models.IntegerField(default='')
    lasttotal = models.IntegerField(default='')
   
