from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_id= models.CharField(max_length=100, unique=True)
    course = models.CharField(max_length=100 )
    section = models.CharField(max_length=20 )
    studying_year = models.CharField(max_length=100)
    graduation=models.CharField(max_length=4)
    photo = models.ImageField(upload_to='images')
    email_address = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return self.first_name +' '+ self.last_name