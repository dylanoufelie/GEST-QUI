from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def connexion(request):
    return render(request,'connexion/connexion.html')