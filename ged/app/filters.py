import django_filters
from .models import Article, Client, Fournisseur,Staff,FichierDoc,Commande,Reception,Facture,Devis,Videos,PDF,Word,Note

class ArticleFilter(django_filters.FilterSet):


    class Meta:
        model= Article
        fields = ('reference','designation','code','type','unite_id')




class ClientFilter(django_filters.FilterSet):
    class Meta:
        model= Client
        fields = ('name','code','pays','ville','telephone')


class FournisseurFilter(django_filters.FilterSet):
    class Meta:
        model= Fournisseur
        fields = ('name','code','pays','ville','telephone')


class StaffFilter(django_filters.FilterSet):
    class Meta:
        model= Staff
        fields = ('services_id','gender','adresse','role')


class FichierDocFilter(django_filters.FilterSet):
    class Meta:
        model= FichierDoc
        fields = ('titre','nature','sujets','expire')


class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model= Commande
        fields = ('reference','Quantite','article_id','fournisseur_id','unite_id')


class ReceptionFilter(django_filters.FilterSet):
    class Meta:
        model= Reception
        fields = ('reference','commande_id','date','actuelle','article_id')


class FactureFilter(django_filters.FilterSet):
    class Meta:
        model= Facture
        fields = ('reference','reception_id','date_f','date_e')



class DevisFilter(django_filters.FilterSet):
    class Meta:
        model= Devis
        fields = ('reference','article_id','client_id','unite_id','date_devis')

class VideoFilter(django_filters.FilterSet):
    class Meta:
        model= Videos
        fields = ('titre','expire','sujets','created_at','updated_at')

class PdfFilter(django_filters.FilterSet):
    class Meta:
        model= PDF
        fields = ('titre','expire','sujets','created_at')


class WordFilter(django_filters.FilterSet):
    class Meta:
        model= Word
        fields = ('titre','expire','sujets','nature')



class NoteFilter(django_filters.FilterSet):
    class Meta:
        model= Note
        fields = ('titre','created_at','description')