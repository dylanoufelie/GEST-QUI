from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .formulaire import Entrepriseform, Clientsform
# Create your views here.


def formulaire(request):
    if request.method == "POST":
        print(request.POST)
        form = Entrepriseform(request.POST).save()
        return redirect('/')
    else:
        form = Entrepriseform()
        print("1")
        return render(request,'formulaire/formulaire.html', {'form': form})

def formulaire_client(request):

    if request.method == 'POST':
        form = Clientsform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Clientsform()
        return render(request,'formulaire/formulaire_client.html', {'form': form})