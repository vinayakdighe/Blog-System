from django.db import models
from django.forms import CharField
# Create your models here.
class reg(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pass1=models.CharField(max_length=50)
    re_pass=models.CharField(max_length=50)

#def __str__(self):
    #return self.name +" "+ self.models.Email +" "
