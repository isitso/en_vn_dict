from django.db import models

# Create your models here.


class Word(models.Model):
    """
    Word model.
    """
    word = models.CharField(max_length=40)
    meaning_vn = models.CharField(max_length=1024)
    type = models.CharField(max_length=50)
    meaning_en = models.CharField(max_length=1024)
