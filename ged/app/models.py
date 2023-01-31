from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField  #add
from django.urls import reverse


class CustomUser(AbstractUser):
    USER=(
        (1,'HOD'),
        (2,'STAFF'),
    )

    user_type=models.CharField(choices=USER,max_length=50, default=1)
    profile_pic=models.ImageField(upload_to='profile_pic')

class Services(models.Model):
        name = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name


class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    adresse = models.TextField()
    services_id = models.ForeignKey(Services, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Client(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    adresse = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True,null=True)
    updated_at= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    adresse = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Unite(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    type = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    cump = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    stock = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100)
    parcourrir=models.ImageField(upload_to='parcourrir')
    unite_id = models.ForeignKey(Unite, on_delete=models.DO_NOTHING)
    prix_ht =  models.CharField(max_length=100, null=True)
    Quantite = models.CharField(max_length=100)
    prix_a = models.CharField(max_length=100)
    prix_v = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.code



class FichierDoc(models.Model):

    titre = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sujets = models.CharField(max_length=100)
    nature = models.CharField(max_length=100)
    couverture = models.CharField(max_length=100)
    expire =  models.CharField(max_length=100)
    contenu=models.ImageField(upload_to='contenu')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class SendEmail(models.Model):
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    document=models.ImageField(upload_to='document')


    def __str__(self):
        return self.email


class Commande(models.Model):
    reference = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    date_c = models.CharField(max_length=100)
    date_r=models.CharField(max_length=100)
    paiement=models.CharField(max_length=100)
    remise=models.CharField(max_length=100)
    tva=models.CharField(max_length=100)
    ttc=models.CharField(max_length=100)
    Quantite = models.CharField(max_length=100)
    prix_a = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    article_id = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    fournisseur_id = models.ForeignKey(Fournisseur, on_delete=models.DO_NOTHING)
    unite_id = models.ForeignKey(Unite, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.reference

class Reception  (models.Model):
    reference = models.CharField(max_length=100)
    commande_id = models.ForeignKey(Commande, on_delete=models.DO_NOTHING)
    note = models.TextField()
    date = models.CharField(max_length=100, null=True)
    actuelle = models.CharField(max_length=100)
    article_id = models.ForeignKey(Article, on_delete=models.DO_NOTHING,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference

class Facture  (models.Model):
    reference = models.CharField(max_length=100)
    reception_id = models.ForeignKey(Reception, on_delete=models.DO_NOTHING)
    date_f = models.CharField(max_length=100)
    date_e = models.CharField(max_length=100 , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference

class Devis(models.Model):
    reference = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    date_devis = models.CharField(max_length=100)
    validite_devis=models.CharField(max_length=100)
    paiement=models.CharField(max_length=100)
    remise=models.CharField(max_length=100)
    tva=models.CharField(max_length=100)
    ttc=models.CharField(max_length=100)
    Quantite = models.CharField(max_length=100)
    prix_vente = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    article_id = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    unite_id = models.ForeignKey(Unite, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.reference


class Note(models.Model):
    titre = models.CharField(max_length=100)
    description = HTMLField()
    photo=models.ImageField(upload_to='photo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Videos(models.Model):
    titre = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sujets = models.CharField(max_length=100)
    couverture = models.CharField(max_length=100)
    expire =  models.CharField(max_length=100)
    video=models.FileField(upload_to='video/%y')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class PDF(models.Model):
    titre = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sujets = models.CharField(max_length=100)
    couverture = models.CharField(max_length=100)
    expire =  models.CharField(max_length=100)
    pdf=models.FileField(upload_to='pdf/%y')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Word(models.Model):
    titre = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sujets = models.CharField(max_length=100)
    nature = models.CharField(max_length=100)
    expire =  models.CharField(max_length=100)
    word=models.FileField(upload_to='word/%y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class PaiementFournisseur  (models.Model):
    reference = models.CharField(max_length=100)
    facture_id = models.ForeignKey(Facture, on_delete=models.DO_NOTHING)
    date_paiement = models.CharField(max_length=100)
    note = models.CharField(max_length=100 , null=True)
    montant = models.CharField(max_length=100 , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference


class StockArticle(models.Model):
    code = models.CharField(max_length=100)
    article_id = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.code

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('Hod:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
