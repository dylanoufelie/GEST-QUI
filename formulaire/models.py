from django.db import models
# Create your models here.
class Entreprise(models.Model):
    Entrprise = models.CharField(max_length=200, null=True)
    Adresse_Email = models.EmailField(max_length=40, null=True)
    telephone = models.IntegerField(max_length=20, null=True)
    banquaire = models.IntegerField(max_length=200, null=True)
    OM = models.IntegerField(max_length=9, null=True)
    MOMO = models.IntegerField(max_length=9, null=True)
    nom_utilisateur = models.CharField(max_length=200, null=True)
    mot_passe = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    confirmer_votre_mot_de_passe = models.CharField(max_length=200, null=True)
class Clients(models.Model):
    nom = models.CharField(max_length=200,null=True)
    prenom = models.CharField(max_length=200,null=True)
    Adresse_Email = models.EmailField(max_length=40, null=True)
    nom_utulisateur = models.CharField(max_length=200,null=True)
    mot_passe = models.CharField(max_length=200, null=True)
    confirmer_votre_mot_de_passe = models.CharField(max_length=200, null=True)