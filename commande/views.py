from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def command(request):
    return render(request,'commande/commande.html')