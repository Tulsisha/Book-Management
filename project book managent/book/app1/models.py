from django.db import models
# Create your models here.
class contactm(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class contactm2(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    def __str__(self):
        return self.username
