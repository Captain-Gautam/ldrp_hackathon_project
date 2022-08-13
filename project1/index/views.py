from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SymptomForm

# Create your views here.


def index(request):
   
    form = SymptomForm()
    if request.method == 'POST':
        print(request.POST)
        form = SymptomForm(request.POST)

        if form.is_valid():
            form.save()
   
    context = {'form':form}

    return render(request, "index/index.html", context)