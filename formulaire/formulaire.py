from django.forms import ModelForm
from .models import Entreprise,Clients


class Entrepriseform(ModelForm):
    class Meta:
        model = Entreprise
        fields = ['Entrprise' , 'Adresse_Email' , 'telephone' , 'banquaire' , 'OM' , 'MOMO' , 'nom_utilisateur' , 'mot_passe']
class Clientsform(ModelForm):
    class Meta:
        model = Clients
        fields = ['nom' , 'prenom' , 'Adresse_Email' , 'nom_utulisateur' , 'mot_passe' , 'confirmer_votre_mot_de_passe']