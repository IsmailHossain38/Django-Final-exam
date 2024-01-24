from django.shortcuts import render,redirect
from .forms import ContectUsForm
# Create your views here.



def contactus(request):
    if request.method == 'POST':
        form = ContectUsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ContectUsForm()
    return render(request, 'contect.html', {'form': form})