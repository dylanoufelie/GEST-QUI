from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def basket(request):
    return render(request,'pagneir/pagnier.html')