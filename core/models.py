from django.db import models

# Create your models here.

class Client(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=16)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.lastName+" "+self.firstName
    
    
        
   
        
