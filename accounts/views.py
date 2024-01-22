from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView 
from django.contrib.auth.models import User
from . import forms
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator 
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.contrib.auth import logout,update_session_auth_hash
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import   PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from tution.models import AddTutors
from django.contrib.auth.decorators import login_required
from . import models
from tution.models import ApplicantForTutor
# Create your views here.

class UserLogin(LoginView):
    template_name = 'register.html'
    def form_valid(self, form):
        messages.success(self.request,"Logged in successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request," Logged information incorrect ")
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('profile')
    
    
def register(request):
    if request.method == 'POST':
        form =forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"https://tutionzone.onrender.com/accounts/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            messages.success(request,"Check Your Email for confirmation. After Confirming your email, you will be able to login.")
        return render(request,'register.html',{'form':form})
    else:
        form =forms.RegistrationForm()
    return render(request,'register.html',{'form':form})

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None  and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
@login_required
def Userlogout(request):
    logout(request)
    return redirect('homepage')


class Profile(LoginRequiredMixin,ListView):
    template_name = 'profile.html'
    model = AddTutors
    context_object_name = 'data'
    def get_queryset(self):
        return AddTutors.objects.filter(user =self.request.user)
    

@login_required
def userPersonalUpdate(request):
    if request.method == 'POST':
        profile_form = forms.UserPersonalForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.user = request.user
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.UserPersonalForm(instance = request.user)
    return render(request, 'edit_personal.html', {'form' : profile_form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'edit_personal.html', {'form' : form})

    

def applyfortution(request, id):
    tutors = get_object_or_404(AddTutors, pk=id)
    try:
        informations = ApplicantForTutor.objects.get(user=request.user)
    except ApplicantForTutor.DoesNotExist:
        informations = ApplicantForTutor.objects.create(
            tutors=tutors,
            user=request.user,
        )
    if informations.admin_approval:
        tutors.user = request.user
        tutors.save()
        messages.success(request, 'You got this Tuition!')
        return redirect('profile')
    else:
        mail_sub = 'Applicant Confirmations'
        message = render_to_string('applicant_pending.html', {'user': request.user})
        to_email = request.user.email
        send_mail = EmailMultiAlternatives(mail_sub, '', to=[to_email])
        send_mail.attach_alternative(message, 'text/html')
        send_mail.send()
        messages.success(request, 'Your application has been successfully sent to admin. Now wait for admin approval.')

        return redirect('profile')