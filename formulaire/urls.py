from django.urls import path
from . import views

urlpatterns = [
    path('/entreprise',views.formulaire ,name='entreprise'),
    path('/client',views.formulaire_client, name='client')
]
