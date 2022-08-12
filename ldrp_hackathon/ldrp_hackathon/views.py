from django.shortcuts import render
from django.shortcuts import HttpResponse


def welcome(request):
    return render(request, "ldrp_hackathon/welcome.html")