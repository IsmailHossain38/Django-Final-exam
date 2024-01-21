
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserInformation
class RegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}) ,required=True)
    qualification = forms.CharField(max_length=100 ,required=True)
    number = forms.CharField(max_length=12 ,required=True)
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']
        
    def save(self, commit=True):
        our_user = super().save(commit=False) 
        
        if commit == True:
            our_user.is_active = False
            our_user.save() 
            qualification = self.cleaned_data.get('qualification')
            number = self.cleaned_data.get('number')
            date_of_birth = self.cleaned_data.get('date_of_birth')
            UserInformation.objects.create(
                user = our_user,
                qualification  = qualification,
                number = number,
                date_of_birth =date_of_birth,
                
            )
            
        
        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
        
        
class UserPersonalForm(UserChangeForm):
    password =None
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    qualification = forms.CharField(max_length=100)
    number = forms.CharField(max_length=12)
    class Meta:
        model =User
        fields=['username','first_name','last_name','email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
         
        if self.instance:
            try:
                user_account = self.instance.userinformation
            except UserInformation.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['qualification'].initial = user_account.qualification
                self.fields['date_of_birth'].initial = user_account.date_of_birth
                self.fields['number'].initial = user_account.number
             

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserInformation.objects.get_or_create(user=user) 
            user_account.qualification = self.cleaned_data['qualification']
            user_account.date_of_birth = self.cleaned_data['date_of_birth']
            user_account.number = self.cleaned_data['number']
            user_account.save()

        return user

