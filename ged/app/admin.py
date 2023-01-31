from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser , UserModel)
admin.site.register(Services)
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(Fournisseur)
admin.site.register(Unite)
admin.site.register(Article)
admin.site.register(FichierDoc)
admin.site.register(SendEmail)
admin.site.register(Commande)
admin.site.register(Reception)
admin.site.register(Facture)
admin.site.register(Devis)
admin.site.register(Note)
admin.site.register(Videos)
admin.site.register(PDF)
admin.site.register(Word)
admin.site.register(PaiementFournisseur)
admin.site.register(StockArticle)
admin.site.register(Event)








