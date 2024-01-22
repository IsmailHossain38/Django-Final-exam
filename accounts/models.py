from django.db import models
from django.contrib.auth.models import User

# Create your models here.


QUALIFICATION_CHOICES = [
    ('HSC_Passed', 'HSC Passed'),
    ('Diploma_in_Computer', 'Diploma in Computer'),
    ('BBA', 'BBA'),
    ('MBA', 'MBA'),
    ('English', 'English'),
    ('Accounting', 'Accounting'),  
]

class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinformation')
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=100, choices=QUALIFICATION_CHOICES)
    number = models.CharField(max_length=12)
    
    def __str__(self) -> str:
        return f"{self.user.username}"
    
    
