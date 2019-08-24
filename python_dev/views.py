from django.shortcuts import render
from django.http import HttpResponse


def index(requete):
    return render(request = requete, template_name = 'index.html')
