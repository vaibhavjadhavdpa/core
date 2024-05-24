from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    standard = models.CharField(max_length=50, blank=True, null=True)
    classs = models.CharField(max_length=1, blank=True, null=True)
    AddarNo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image =models.ImageField()
    file = models.FileField() 
    Yearsofexperience  = models.IntegerField()
    
