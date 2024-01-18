from django.db import models
from django.contrib.auth.models import User
from categorybyclasses.models import CategoryByClasses

# Create your models here.
EXPERIENCE = [
    ('None'),('None'),
    ('1 Years'),('1 Years'),
    ('2 Years'),('2 Years'),
    ('3 Years'),('3 Years'),
    ('4 Years'),('4 Years'),
    ('5 Years'),('5 Years'),
    ('More'),('More'),
]

class AddTutors(models.Model): 
    user = models.ForeignKey(User,on_delete =models.CASCADE,related_name ='tutor')
    name =models.CharField(max_length=50)
    image = models.ImageField(upload_to="tution/image/")
    class_category = models.ManyToManyField(CategoryByClasses)
    education = models.CharField(max_length=100)
    teaching_experience = models.CharField(max_length =20)
    fee =models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    number =models.CharField(max_length=12)
    
    def __str__(self) -> str:
        return self.name

class ApplicantForTutor(models.Model):
    tutors = models.ForeignKey(AddTutors,on_delete =  models.CASCADE, related_name='applicant')
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    admin_approval = models.BooleanField(default=False)
    
    def __str__(self):
        return f"User : {self.user.username} Tutor : {self.tutors.name}"
    
    
    
STARCHOICES =[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    # reviewers = models.ForeignKey(User ,on_delete =  models.CASCADE)
    tutors = models.ForeignKey(AddTutors ,on_delete =  models.CASCADE, related_name='reviews')
    body = models.TextField()
    name= models.CharField(max_length=100)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices = STARCHOICES ,max_length =10)
    def __str__(self) -> str:
        return self.tutors.user.username