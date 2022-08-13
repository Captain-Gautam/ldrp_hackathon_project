
from dataclasses import fields
from django.forms import ModelForm
from .models import Symptom

class SymptomForm(ModelForm):
    class Meta:
        model = Symptom
        fields = ['symptom1']