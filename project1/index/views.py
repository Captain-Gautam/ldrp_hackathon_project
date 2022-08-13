from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import Symptom
from .forms import SymptomForm

# Create your views here.


def index(request):
   
    form = SymptomForm()
    if request.method == 'POST':
        symptom1 = request.POST['symptom1']
        print(symptom1)
        form = SymptomForm(request.POST)

        if form.is_valid():
            form.save()
   
    context = {'form':form}

    return render(request, "index/index.html", context)