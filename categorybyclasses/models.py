from django.db import models

# Create your models here.
class CategoryByClasses(models.Model):
    name = models.CharField(max_length =30)
    slug = models.SlugField(max_length =40)
    
    def __str__(self) -> str:
        return self.name