from django.db import models

# Create your models here.
symptomsF= (
    ('Heart Disease','Heart Diseases'),
    ('Breast Cancer','Breast Cancer'),
    ('Ovarian and Cervical Cancer','Ovarian and Cervical Cancer'),
    ('Gynecological Health','Gynecological Health'),
    ('Pregnancy Issues','Pregnancy Issues'),
    ('Depression and Anxiety','Depression and Anxiety'),
    ('Pneumonia','Pneumonia'),
    ('Diarrhoe','Diarrhoe'),
    ('Malaria','Malaria'),
    ('Tuberculosis','Tuberculosis'),
    ('Chickenpox','Chickenpox'),
    ('Whooping cough','Whooping cough'),
    ('Common Cold','Common Cold'),
    ('Ear infection','Ear infection'),
    ('Gastroenteritis','Gastroenteritis'),
    ('Influenza (flu)','Influenza (flu)'),
    ('Strep throat','Strep throat'),
    ('Mononucleosis','Mononucleosis'),
    ('Gastroenteritis','Gastroenteritis'),
    ('Anxiety','Anxiety'),
    ('Asthma','Asthma'),
    ('Cancer','Cancer'),
    ('Allergy','Allergy'),
    ('Gonorrhea','Gonorrhea'),
    ('Syphilis','Syphilis'),
    ('HIV','HIV'),
    ('Chlamydia','Chlamydia'),
)

class Symptom(models.Model):
     symptom1 = models.CharField(max_length=50, choices=symptomsF)