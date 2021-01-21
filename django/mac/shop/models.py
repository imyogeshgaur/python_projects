from django.db import models

# Create your models here

class student(models.Model):
    roll_no = models.AutoField
    name = models.CharField(max_length = 50)
    School = models.CharField(max_length = 300)
    date = models.DateField()
