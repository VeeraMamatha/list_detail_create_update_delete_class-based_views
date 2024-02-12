from django.db import models

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    def __str__(self):
        return self.sname

class student(models.Model):
    stname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sname=models.ForeignKey(school,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.stname
