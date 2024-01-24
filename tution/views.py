from django.shortcuts import render,redirect
from .models import AddTutors
from django.views.generic import DetailView 
from django.contrib import messages
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def tutorDetails(request,id):
    tutors =AddTutors.objects.get(pk=id)
    review = tutors.reviews.all()
    return render(request,'tutor_detail/details.html',{'tution':tutors ,"review":review})
def about_us(request):
    return render(request,'tutor_detail/about_us.html')




class TutorDetails(LoginRequiredMixin,DetailView):
    model = AddTutors
    pk_url_kwarg = 'id'
    template_name = 'review.html'
    def post(self,request,*args, **kwargs):
        tutors=self.get_object()
        review_form = forms.ReviewForm(data=self.request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.tutors = tutors
            new_review.save()
            messages.success(request,"Your review has been successful")
            
        return self.get(request,*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tutors = self.object
        review = tutors.reviews.all()
        review_form = forms.ReviewForm()
        # context['tution'] = tutor
        context['review_form'] = review_form
        # context['review'] = review
        return context
    