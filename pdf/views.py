from django.shortcuts import render, redirect
from .models import Profile
from .forms import *
# Create your views here.


def accept(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = ProfileForm()
    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_form = Profile.objects.get(pk=id)
    return render(request, 'pdf/resume.html', {'user_form': user_form})
