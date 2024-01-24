from django.db import models

# Create your models here.
class ContectUsModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    Number = models.CharField(max_length=12)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.name