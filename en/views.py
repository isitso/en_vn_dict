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

    def get_queryset(self):
        char = self.args[0]
        if char != None:
            return models.Word.objects.filter(word__startswith=char)
        return super().get_queryset()
