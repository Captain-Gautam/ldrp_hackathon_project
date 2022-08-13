from django.db import models

# Create your models here.
COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


class Symptom(models.Model):
     symptom1 = models.CharField(max_length=50, choices=COLOR_CHOICES,)
   