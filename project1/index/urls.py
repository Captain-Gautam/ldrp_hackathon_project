from index import views
from django.urls import URLPattern, path
#from django.conf.urls import url
from . import views

urlpatterns = [
    path("",views.index, name= "index"),
]