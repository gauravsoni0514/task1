"""from django.shortcuts import render,redirect
from fileup.models import Inputfile
from fileup.form import InputfileForm

def showfile(request):
 #   if request.method == "POST":

        lastfile = Inputfile.objects.last()

        ufile = lastfile.ufile

        ufile = lastfile.uname

        form = InputfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context = {'ufile': ufile,
               'form': form,
               'filename': filename
               }

        return render(request, 'index.html', context)
"""

"""from django.shortcuts import render,redirect
from fileup.form import InputfileForm
from fileup.models import Inputfile
from django.core.files import File
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse


def showfile(request):
    if request.method == "POST":
        form=InputfileForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                ufile = Inputfile(ufile=request.FILES['ufile'])

                ufile.save()
                return HttpResponseRedirect(reverse('showfile'))
            except:
                pass
    else:
        form=InputfileForm()
    return render(request,"index.html",{'form':form})
"""
"""class UploadFileForm(forms.Form):
	file = forms.FileField()
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			file_in_memory = request.FILES['file'].read()
"""


"""
from django.shortcuts import render,redirect
from fileup.form import InputfileForm
from fileup.models import Inputfile


def showfile(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyInputfileForm = InputfileForm(request.POST, request.FILES)

        if MyInputfileForm.is_valid():
            inputfile = Inputfile()
            inputfile.uname = MyInputfileForm.cleaned_data["uname"]
            inputfile.ufile = MyInputfileForm.cleaned_data["ufile"]
            inputfile.save()
            saved = True
    else:
        MyInputfileForm = InputfileForm()

    return render(request, 'index.html', locals())
"""





"""from django.http import HttpResponse
from django.shortcuts import render,redirect
from fileup.form import InputfileForm
from fileup.models import Inputfile
from django.core.files import File
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from fileup.models import *
def showfile(request):
    saved = False
    if request.method == 'POST':
        MyInputfile = InputfileForm(request.POST, request.FILES)
        if MyInputfile.is_valid():
            inputfile=Inputfile()
            inputfile.uname=MyInputfile.clean_data["unmae"]
            inputfile.ufile=MyInputfile.clean_data["ufile"]
            inputfile.save()
            saved=True
        return redirect('wlcm')
    else:
        MyInputfile = InputfileForm()
    return render(request, "index.html", locals())


def wlcm(request):
    return render(request,'wlcm.html')
"""

import csv
from django.shortcuts import render,redirect
from fileup.form import InputfileForm
from fileup.models import Inputfile
from django.core.exceptions import ValidationError
def showfile(request):
    if request.method=="GET":

        form=InputfileForm(request.GET,request.FILES['ufile'])
        if form.is_valid():
            file = open("ufile")
            numline = len(file.readlines())
            print(numline)
            if numline < 300:
                raise ValidationError("The maximum file length that can be uploaded is more than 300 rows")
            else:
                print("file is verify")
            form.save()
            return redirect("/wcm")
    else:
        form=InputfileForm()
    return render(request,"index.html",{'form':form})

def wcm(request):
    inputfile=Inputfile.objects.all()
    return render(request,"wcm.html",{'inputfile':inputfile})

