from django.shortcuts import render
from . import models
from django.views import generic
# Create your views here.

class WordView(generic.ListView):
    """
    Word list
    """
    model = models.Word
    template_name = 'en/index.html'
