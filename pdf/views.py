from django.shortcuts import render, redirect
from .models import Profile
from .forms import *
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io, os
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
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_form': user_form})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    config = pdfkit.configuration(wkhtmltopdf='C:\\Users\\MT1ShotYT\\Desktop\\CV_Generator\\wkhtmltox\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options,configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"

    return response


def user_lists(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})
