
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Services, CustomUser, Staff, Client, Fournisseur, Article, Unite, FichierDoc, SendEmail,Commande, Reception, Facture, Devis, Note, Videos, PDF, Word, PaiementFournisseur,StockArticle,Event
from django.contrib import messages
from django.http import HttpResponse
import datetime
import csv
from django.views import generic
from django.utils.safestring import mark_safe
from app.filters import ArticleFilter, ClientFilter, FournisseurFilter, StaffFilter, FichierDocFilter, CommandeFilter,ReceptionFilter, FactureFilter, DevisFilter, VideoFilter, PdfFilter, WordFilter,NoteFilter

from .utils import Calendar
from datetime import datetime, timedelta


@login_required(login_url='/')
def Home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        video = Videos.objects.filter(titre__icontains=q)
    user_count=Staff.objects.all().count()
    article_count=Article.objects.all().count()
    fournisseurs_count=Fournisseur.objects.all().count()
    client_count=Client.objects.all().count()
    staff=Staff.objects.all()
    image_count=FichierDoc.objects.all().count()
    video_count=Videos.objects.all().count()
    pdf_count=PDF.objects.all().count()
    word_count=Word.objects.all().count()
    article=Article.objects.all()
    video= Videos.objects.all()
    commande=Commande.objects.all().count()
    stock=StockArticle.objects.all().count()
    fichierdoc = FichierDoc.objects.all()
    context = {
       'user_count':user_count,
        'commande':commande,
        'article_count':article_count,
        'fournisseurs_count':fournisseurs_count,
        'client_count':client_count,
        'staff':staff,
        'image_count':image_count,
        'video_count':video_count,
        'pdf_count':pdf_count,
        'word_count':word_count,
        'article':article,
        'fichierdoc':fichierdoc,
        'video':video,
        'stock':stock,
    }

    return render(request, 'Hod/home.html',context)

@login_required(login_url='/')
def Add_User(request):
    services = Services.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        adresse = request.POST.get('adresse')
        services_id = request.POST.get('services_id')
        role = request.POST.get('role')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_user')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_user')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            services = Services.objects.get(id=services_id)

            staff = Staff(
                admin=user,
                adresse=adresse,
                services_id=services,
                role=role,
                gender=gender,
            )
            staff.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('view_user')
    context = {
        'services': services,
    }

    return render(request, 'Hod/add_users.html', context)


@login_required(login_url='/')
def View_User(request):
    staff = Staff.objects.all()
    myFilter = StaffFilter(request.GET, queryset=staff)
    staff = myFilter.qs
    context = {
        "staff": staff,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_user.html', context)

@login_required(login_url='/')
def Delete_User(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_user')


@login_required(login_url='/')
def Edit_User(request, id):
    staff = Staff.objects.filter(id=id)
    services = Services.objects.all()
    context = {
        'staff': staff,
        'services': services,
    }
    return render(request, 'Hod/edit_user.html', context)


@login_required(login_url='/')
def Update_User(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        print(staff_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        adresse = request.POST.get('adresse')
        gender = request.POST.get('gender')
        role = request.POST.get('role')
        services_id = request.POST.get('services_id')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.adresse = adresse

        services = Services.objects.get(id=services_id)
        staff.services_id = services

        staff.gender = gender
        staff.role=role

        staff.save()
        messages.success(request, 'successufully Update')
        return redirect('view_user')

    return render(request, 'Hod/edit_user.html')


@login_required(login_url='/')
def Add_Client(request):
    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        code_postal = request.POST.get('code_postal')
        fax = request.POST.get('fax')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        adresse = request.POST.get('adresse')

        client = Client(
            code=code,
            name=name,
            email=email,
            telephone=telephone,
            code_postal=code_postal,
            fax=fax,
            pays=pays,
            ville=ville,
            adresse=adresse,
        )
        client.save()
        messages.success(request, 'successufully added ')
        return redirect('add_client')

    return render(request, 'Hod/add_client.html')


def View_Client(request):
    client = Client.objects.all()
    myFilter = ClientFilter(request.GET, queryset=client)
    client = myFilter.qs

    context = {
        'client': client,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_client.html', context)


@login_required(login_url='/')
def Delete_Client(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_client')


@login_required(login_url='/')
def Edit_Client(request, id):
    client = Client.objects.filter(id=id)

    context = {
        'client': client,

    }
    return render(request, 'Hod/edit_client.html', context)


@login_required(login_url='/')
def Update_Client(request):
    if request.method == "POST":
        code = request.POST.get('code')
        client_id = request.POST.get('client_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        code_postal = request.POST.get('code_postal')
        fax = request.POST.get('fax')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        adresse = request.POST.get('adresse')

        client = Client(
            code=code,
            id=client_id,
            name=name,
            email=email,
            telephone=telephone,
            code_postal=code_postal,
            fax=fax,
            pays=pays,
            ville=ville,
            adresse=adresse,
        )
        client.save()
        messages.success(request, 'successufully Update')
        return redirect('view_client')

    return render(request, 'Hod/edit_client.html')


@login_required(login_url='/')
def Export_Excel(request):
    response = HttpResponse(content_type='')
    response['Content-Disposition'] = 'attachement ; filename = Client' + \
                                      str(datetime.datetime.now()) + '.csv'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Code', 'Name', 'email', 'telephone', 'code_postal', 'fax', 'pays', 'ville', 'adresse'])

    clients = Client.objects.filter(name=request.user)

    for client in clients:
        writer.writerow(
            [client.id, client.code, client.name, client.email, client.telephone, client.code_postal, client.fax,
             client.pays, client.ville, client.adresse])

    return response


@login_required(login_url='/')
def Add_Fournisseur(request):
    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        code_postal = request.POST.get('code_postal')
        fax = request.POST.get('fax')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        adresse = request.POST.get('adresse')

        fournisseur = Fournisseur(
            code=code,
            name=name,
            email=email,
            telephone=telephone,
            code_postal=code_postal,
            fax=fax,
            pays=pays,
            ville=ville,
            adresse=adresse,
        )
        fournisseur.save()
        messages.success(request, 'successufully added ')
        return redirect('view_fournisseur')

    return render(request, 'Hod/add_fournisseur.html')


@login_required(login_url='/')
def View_Fournisseur(request):
    fournisseur = Fournisseur.objects.all()
    myFilter = FournisseurFilter(request.GET, queryset=fournisseur)
    fournisseur = myFilter.qs

    context = {
        'fournisseur': fournisseur,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_fournisseur.html', context)


@login_required(login_url='/')
def Delete_Fournisseur(request, id):
    fournisseur = Fournisseur.objects.get(id=id)
    fournisseur.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_fournisseur')


@login_required(login_url='/')
def Edit_Fournisseur(request, id):
    fournisseur = Fournisseur.objects.filter(id=id)

    context = {
        'fournisseur': fournisseur,

    }
    return render(request, 'Hod/edit_fournisseur.html', context)


@login_required(login_url='/')
def Update_Fournisseur(request):
    if request.method == "POST":
        code = request.POST.get('code')
        fournisseur_id = request.POST.get('fournisseur_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        code_postal = request.POST.get('code_postal')
        fax = request.POST.get('fax')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        adresse = request.POST.get('adresse')

        fournisseur = Fournisseur(
            code=code,
            id=fournisseur_id,
            name=name,
            email=email,
            telephone=telephone,
            code_postal=code_postal,
            fax=fax,
            pays=pays,
            ville=ville,
            adresse=adresse,
        )
        fournisseur.save()
        messages.success(request, 'successufully Update')
        return redirect('view_fournisseur')

    return render(request, 'Hod/edit_fournisseur.html')


@login_required(login_url='/')
def Export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement ; filename = Fournisseur' + \
                                      str(datetime.datetime.now()) + '.csv'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Code', 'Name', 'email', 'telephone', 'code_postal', 'fax', 'pays', 'ville', 'adresse'])

    fournisseurs = Fournisseur.objects.filter(name=request.user)

    for fournisseur in fournisseurs:
        writer.writerow([fournisseur.id, fournisseur.code, fournisseur.name, fournisseur.email, fournisseur.telephone,
                         fournisseur.code_postal, fournisseur.fax, fournisseur.pays, fournisseur.ville,
                         fournisseur.adresse])

    return response


@login_required(login_url='/')
def Add_Article(request):
    unite = Unite.objects.all()

    if request.method == "POST":
        parcourrir = request.FILES.get('parcourrir')
        type = request.POST.get('type')
        code = request.POST.get('code')
        reference = request.POST.get('reference')
        cump = request.POST.get('cump')
        stock = request.POST.get('stock')
        designation = request.POST.get('designation')
        prix_ht = request.POST.get('prix_ht')
        unite_id = request.POST.get('unite_id')
        Quantite = request.POST.get('Quantite')
        prix_a = request.POST.get('prix_a')
        prix_v = request.POST.get('prix_v')

        unite = Unite.objects.get(id=unite_id)

        article = Article(
            parcourrir=parcourrir,
            type=type,
            code=code,
            reference=reference,
            cump=cump,
            stock=stock,
            designation=designation,
            prix_ht=prix_ht,
            Quantite=Quantite,
            prix_a=prix_a,
            prix_v=prix_v,
            unite_id=unite,
        )
        article.save()
        messages.success(request, 'successufully added ')
        return redirect('view_article')

    context = {
        'unite': unite,

    }
    return render(request, 'Hod/add_article.html', context)


@login_required(login_url='/')
def View_Article(request):
    article = Article.objects.all()
    myFilter = ArticleFilter(request.GET, queryset=article)
    article = myFilter.qs

    context = {
        'article': article,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_article.html', context)


@login_required(login_url='/')
def Delete_Article(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_article')


@login_required(login_url='/')
def Edit_Article(request, id):
    article = Article.objects.filter(id=id)

    context = {
        'article': article,

    }
    return render(request, 'Hod/edit_article.html', context)


@login_required(login_url='/')
def Update_Article(request):
    unite = Unite.objects.all()

    if request.method == "POST":
        parcourrir = request.FILES.get('parcourrir')
        type = request.POST.get('type')
        article_id = request.POST.get('article_id')
        code = request.POST.get('code')
        reference = request.POST.get('reference')
        cump = request.POST.get('cump')
        stock = request.POST.get('stock')
        designation = request.POST.get('designation')
        prix_ht = request.POST.get('prix_ht')
        unite_id = request.POST.get('unite_id')
        Quantite = request.POST.get('Quantite')
        prix_a = request.POST.get('prix_a')
        prix_v = request.POST.get('prix_v')

        unite = Unite.objects.get(id=unite_id)

        article = Article(
            parcourrir=parcourrir,
            type=type,
            id=article_id,
            code=code,
            reference=reference,
            cump=cump,
            stock=stock,
            designation=designation,
            prix_ht=prix_ht,
            unite_id=unite,
            Quantite=Quantite,
            prix_a=prix_a,
            prix_v=prix_v,
        )
        article.save()
        messages.success(request, 'successufully added ')
        return redirect('view_article')

    context = {
        'unite': unite,
    }
    return render(request, 'Hod/edit_article.html', context)


@login_required(login_url='/')
def Voir_Article(request, id):
    article = Article.objects.filter(id=id)

    context = {
        'article': article,
    }
    return render(request, 'Hod/details_article.html', context)


@login_required(login_url='/')
def Add_Fichier(request):
    if request.method == "POST":
        contenu = request.FILES.get('contenu')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        nature = request.POST.get('nature')
        sujets = request.POST.get('sujets')

        expire = request.POST.get('expire')

        fichierdoc = FichierDoc(
            contenu=contenu,
            titre=titre,
            description=description,
            nature=nature,
            sujets=sujets,

            expire=expire,

        )
        fichierdoc.save()
        messages.success(request, 'successufully added ')
        return redirect('view_fichier')

    return render(request, 'Hod/add_fichier.html')


@login_required(login_url='/')
def View_Fichier(request):
    fichierdoc = FichierDoc.objects.all()
    myFilter = FichierDocFilter(request.GET, queryset=fichierdoc)
    fichierdoc = myFilter.qs
    context = {
        'fichierdoc': fichierdoc,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_fichier.html', context)


@login_required(login_url='/')
def Voir_Fichier(request, id):
    fichierdoc = FichierDoc.objects.filter(id=id)

    context = {
        'fichierdoc': fichierdoc,
    }
    return render(request, 'Hod/details_fichier.html', context)


@login_required(login_url='/')
def Edit_Fichier(request, id):
    fichierdoc = FichierDoc.objects.filter(id=id)

    context = {
        'fichierdoc': fichierdoc,
    }
    return render(request, 'Hod/edit_fichier.html', context)


@login_required(login_url='/')
def Update_Fichier(request):
    if request.method == "POST":
        contenu = request.FILES.get('contenu')
        fichier_id = request.POST.get('fichier_id')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        nature = request.POST.get('nature')
        sujets = request.POST.get('sujets')
        expire = request.POST.get('expire')

        fichierdoc = FichierDoc(
            contenu=contenu,
            id=fichier_id,
            titre=titre,
            description=description,
            nature=nature,
            sujets=sujets,
            expire=expire,

        )
        fichierdoc.save()
        messages.success(request, 'successufully added ')
        return redirect('view_fichier')

    return render(request, 'Hod/edit_fichier.html')


@login_required(login_url='/')
def Delete_Fichier(request, id):
    fichierdoc = FichierDoc.objects.get(id=id)
    fichierdoc.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_fichier')


@login_required(login_url='/')
def Send_Fichier(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']

        send_fichier=SendEmail(
            email=email,
            message=message,
            subject=subject,
        )
        send_fichier.save()
        messages.success(request, 'successufully added ')

    return render(request, 'Hod/send.html')

@login_required(login_url='/')
def Add_Commande(request):
    fournisseur = Fournisseur.objects.all()
    article = Article.objects.all()
    unite = Unite.objects.all()

    if request.method == "POST":
        reference = request.POST.get('reference')
        fournisseur_id = request.POST.get('fournisseur_id')
        date_c = request.POST.get('date_c')
        date_r = request.POST.get('date_r')
        condition = request.POST.get('condition')
        paiement = request.POST.get('paiement')
        article_id = request.POST.get('article_id')
        unite_id = request.POST.get('unite_id')
        Quantite = request.POST.get('Quantite')
        prix_a = request.POST.get('prix_a')
        remise = request.POST.get('remise')
        tva = request.POST.get('tva')
        ttc = request.POST.get('ttc')

        fournisseur = Fournisseur.objects.get(id=fournisseur_id)
        article = Article.objects.get(id=article_id)
        unite = Unite.objects.get(id=unite_id)

        commande = Commande(
            reference=reference,
            fournisseur_id=fournisseur,
            date_c=date_c,
            date_r=date_r,
            condition=condition,
            paiement=paiement,
            unite_id=unite,
            article_id=article,
            Quantite=Quantite,
            prix_a=prix_a,
            remise=remise,
            tva=tva,
            ttc=ttc,

        )
        commande.save()
        messages.success(request, 'successufully added ')
        return redirect('view_commande')
    context = {
        'fournisseur': fournisseur,
        'article': article,
        'unite': unite,
    }
    return render(request, 'Hod/add_commande.html', context)


@login_required(login_url='/')
def View_Commande(request):
    commande = Commande.objects.all()

    myFilter = CommandeFilter(request.GET, queryset=commande)
    commande = myFilter.qs
    context = {
        'commande': commande,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_commande.html', context)


@login_required(login_url='/')
def Voir_Commande(request, id):
    commande = Commande.objects.filter(id=id)
    context = {
        'commande': commande,
    }
    return render(request, 'Hod/voir_commande.html', context)


@login_required(login_url='/')
def Delete_Commande(request, id):
    commande = Commande.objects.get(id=id)
    commande.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_commande')


@login_required(login_url='/')
def Edit_Commande(request, id):
    unite = Unite.objects.filter(id=id)
    fournisseur = Fournisseur.objects.filter(id=id)
    commande = Commande.objects.filter(id=id)
    context = {
        'commande': commande,
        'fournisseur': fournisseur,
        'unite': unite,
    }
    return render(request, 'Hod/edit_commande.html', context)


@login_required(login_url='/')
def Update_Commande(request):
    fournisseur = Fournisseur.objects.all()

    if request.method == "POST":
        commande_id = request.POST.get('commande_id')
        reference = request.POST.get('reference')
        fournisseur_id = request.POST.get('fournisseur_id')
        date_c = request.POST.get('date_c')
        date_r = request.POST.get('date_r')
        condition = request.POST.get('condition')
        paiement = request.POST.get('paiement')
        Quantite = request.POST.get('Quantite')
        prix_a = request.POST.get('prix_a')
        remise = request.POST.get('remise')
        tva = request.POST.get('tva')
        ttc = request.POST.get('ttc')

        fournisseur = Fournisseur.objects.get(id=fournisseur_id)

        commande = Commande(
            id=commande_id,
            reference=reference,
            fournisseur_id=fournisseur,
            date_c=date_c,
            date_r=date_r,
            condition=condition,
            paiement=paiement,
            Quantite=Quantite,
            prix_a=prix_a,
            remise=remise,
            tva=tva,
            ttc=ttc,

        )
        commande.save()
        messages.success(request, 'successufully added ')
        return redirect('add_commande')
    context = {
        'fournisseur': fournisseur,
    }

    return render(request, 'Hod/edit_commande.html', context)


@login_required(login_url='/')
def Add_Reception_c(request, id):
    reception = Reception.objects.filter(id=id)
    commande = Commande.objects.filter(id=id)
    article = Article.objects.filter(id=id)

    context = {
        'reception': reception,
        'commande': commande,
        'article': article,
    }
    return render(request, 'Hod/add_reception.html', context)


@login_required(login_url='/')
def Add_Reception(request):
    commande = Commande.objects.all()

    if request.method == "POST":
        reference = request.POST.get('reference')
        commande_id = request.POST.get('commande_id')
        date = request.POST.get('date')
        note = request.POST.get('note')
        actuelle = request.POST.get('actuelle')

        commande = Commande.objects.get(id=commande_id)

        reception = Reception(
            reference=reference,
            commande_id=commande,
            date=date,
            note=note,
            actuelle=actuelle,
        )
        reception.save()
        messages.success(request, 'successufully added ')
        return redirect('view_reception')

    context = {
        'commande': commande,

    }
    return render(request, 'Hod/add_reception.html', context)


def View_Reception(request):
    reception = Reception.objects.all()
    myFilter = ReceptionFilter(request.GET, queryset=reception)
    reception = myFilter.qs
    context = {
        'reception': reception,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_reception.html', context)


def Delete_Reception(request, id):
    reception = Reception.objects.get(id=id)
    reception.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_reception')


def Voir_Reception(request, id):
    reception = Reception.objects.filter(id=id)
    context = {
        'reception': reception,
    }
    return render(request, 'Hod/voir_reception.html', context)


def Edit_Reception(request, id):
    article = Article.objects.filter(id=id)
    commande = Commande.objects.filter(id=id)
    reception = Reception.objects.filter(id=id)
    context = {
        'reception': reception,
        'commande': commande,
        'article': article,
    }
    return render(request, 'Hod/edit_reception.html', context)


def Update_Reception(request):
    commande = Commande.objects.all()

    if request.method == "POST":
        reference = request.POST.get('reference')
        commande_id = request.POST.get('commande_id')
        date = request.POST.get('date')
        note = request.POST.get('note')
        actuelle = request.POST.get('actuelle')

        commande = Commande.objects.get(id=commande_id)

        reception = Reception(
            reference=reference,
            commande_id=commande,
            date=date,
            note=note,
            actuelle=actuelle,
        )
        reception.save()
        messages.success(request, 'successufully added ')
        return redirect('view_reception')

    context = {
        'commande': commande,

    }
    return render(request, 'Hod/edit_reception.html', context)


def Add_Facture_f(request, id):
    facture = Facture.objects.filter(id=id)
    reception = Reception.objects.filter(id=id)
    commande = Commande.objects.filter(id=id)
    article = Article.objects.filter(id=id)

    context = {
        'facture': facture,
        'reception': reception,
        'commande': commande,
        'article': article,
    }
    return render(request, 'Hod/add_facture.html', context)


def Add_Facture(request):
    reception = Reception.objects.all()

    if request.method == "POST":
        reference = request.POST.get('reference')
        date_f = request.POST.get('date_f')
        date_e = request.POST.get('date_e')
        reception_id = request.POST.get('reception_id')

        reception = Reception.objects.get(id=reception_id)

        facture = Facture(
            reference=reference,
            reception_id=reception,
            date_f=date_f,
            date_e=date_e,
        )
        facture.save()
        messages.success(request, 'successufully added ')
        return redirect('add_facture')

    context = {
        'reception': reception,
    }
    return render(request, 'Hod/add_facture.html', context)


def View_Facture(request):
    facture = Facture.objects.all()
    myFilter = FactureFilter(request.GET, queryset=facture)
    facture = myFilter.qs
    context = {
        'facture': facture,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_facture.html', context)


def Delete_Facture(request, id):
    facture = Facture.objects.get(id=id)
    facture.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_facture')


def Edit_Facture(request, id):
    facture = Facture.objects.filter(id=id)
    reception = Reception.objects.filter(id=id)
    commande = Commande.objects.filter(id=id)
    article = Article.objects.filter(id=id)

    context = {
        'facture': facture,
        'reception': reception,
        'commande': commande,
        'article': article,
    }
    return render(request, 'Hod/edit_facture.html', context)


def Update_Facture(request):
    reception = Reception.objects.all()

    if request.method == "POST":
        facture_id = request.POST.get('facture_id')
        reference = request.POST.get('reference')
        date_f = request.POST.get('date_f')
        date_e = request.POST.get('date_e')
        reception_id = request.POST.get('reception_id')

        reception = Reception.objects.get(id=reception_id)

        facture = Facture(
            id=facture_id,
            reference=reference,
            reception_id=reception,
            date_f=date_f,
            date_e=date_e,
        )

        facture.save()
        messages.success(request, 'successufully added ')
        return redirect('view_facture')
    context = {
        'reception': reception,
    }
    return render(request, 'Hod/edit_facture.html', context)


def Details_Facture(request, id):
    facture = Facture.objects.filter(id=id)
    context = {
        'facture': facture,
    }
    return render(request, 'Hod/details_facture.html', context)


@login_required(login_url='/')
def Add_Devis(request):
    client = Client.objects.all()
    article = Article.objects.all()
    unite = Unite.objects.all()

    if request.method == "POST":
        reference = request.POST.get('reference')
        client_id = request.POST.get('client_id')
        date_devis = request.POST.get('date_devis')
        validite_devis = request.POST.get('validite_devis')
        condition = request.POST.get('condition')
        paiement = request.POST.get('paiement')
        article_id = request.POST.get('article_id')
        unite_id = request.POST.get('unite_id')
        Quantite = request.POST.get('Quantite')
        prix_vente = request.POST.get('prix_vente')
        remise = request.POST.get('remise')
        tva = request.POST.get('tva')
        ttc = request.POST.get('ttc')

        client = Client.objects.get(id=client_id)
        article = Article.objects.get(id=article_id)
        unite = Unite.objects.get(id=unite_id)

        devis = Devis(
            reference=reference,
            client_id=client,
            date_devis=date_devis,
            validite_devis=validite_devis,
            condition=condition,
            paiement=paiement,
            unite_id=unite,
            article_id=article,
            Quantite=Quantite,
            prix_vente=prix_vente,
            remise=remise,
            tva=tva,
            ttc=ttc,

        )
        devis.save()
        messages.success(request, 'successufully added ')
        return redirect('view_devis')

    context = {
        'client': client,
        'article': article,
        'unite': unite,

    }
    return render(request, 'Hod/add_devis.html', context)


def View_Devis(request):
    devis = Devis.objects.all()
    article = Article.objects.all()
    unite = Unite.objects.all()
    client = Client.objects.all()
    context = {
        'devis': devis,
        'article': article,
        'unite': unite,
        'client': client,
    }
    return render(request, 'Hod/add_devis.html', context)


def Delete_Devis(request, id):
    devis = Devis.objects.get(id=id)
    devis.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_devis')


def View_Devis_V(request):
    devis = Devis.objects.all()
    myFilter = DevisFilter(request.GET, queryset=devis)
    devis = myFilter.qs
    context = {
        'devis': devis,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_devis.html', context)

@login_required(login_url='/')
def Delete_Devis_v(request, id):
    devis = Devis.objects.get(id=id)
    devis.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_devis_v')

@login_required(login_url='/')
def Details_Devis(request, id):
    devis = Devis.objects.filter(id=id)
    context = {
        'devis': devis,
    }
    return render(request, 'Hod/details_devis.html', context)


@login_required(login_url='/')
def Edit_Devis(request, id):
    devis = Devis.objects.filter(id=id)
    client = Client.objects.filter(id=id)
    unite = Unite.objects.filter(id=id)
    context = {
        'devis': devis,
        'client': client,
        'unite': unite,
    }
    return render(request, 'Hod/edit_devis.html', context)


@login_required(login_url='/')
def Update_Devis(request):
    client = Client.objects.all()

    if request.method == "POST":
        devis_id = request.POST.get('devis_id')
        reference = request.POST.get('reference')
        client_id = request.POST.get('client_id')
        date_devis = request.POST.get('date_devis')
        validite_devis = request.POST.get('validite_devis')
        condition = request.POST.get('condition')
        paiement = request.POST.get('paiement')
        Quantite = request.POST.get('Quantite')
        prix_vente = request.POST.get('prix_vente')
        remise = request.POST.get('remise')
        tva = request.POST.get('tva')
        ttc = request.POST.get('ttc')

        client = Client.objects.get(id=client_id)
        devis = Devis(
            id=devis_id,
            reference=reference,
            client_id=client,
            date_devis=date_devis,
            validite_devis=validite_devis,
            condition=condition,
            paiement=paiement,
            Quantite=Quantite,
            prix_vente=prix_vente,
            remise=remise,
            tva=tva,
            ttc=ttc,
        )
        devis.save()
        messages.success(request, 'successufully added ')
        return redirect('view_devis_v')
    context = {
        'client': client,
    }
    return render(request, 'Hod/edit_devis.html', context)

@login_required(login_url='/')
def Note_Add(request):
    if request.method == "POST":
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        note = Note(
            titre=titre,
            description=description,
            photo=photo,
        )
        note.save()
        messages.success(request, 'successufully added ')
        return redirect('note_add')
    return render(request, 'Hod/add_note.html')

def View_Note(request):
    note = Note.objects.all()
    myFilter = NoteFilter(request.GET, queryset=note)
    note = myFilter.qs
    context={
        'note':note,
        'myFilter':myFilter,
    }
    return render(request, 'Hod/note.html',context)

def Delete_Note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_note')

def Add_Video(request):
    if request.method == "POST":
        video = request.FILES.get('video')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        sujets = request.POST.get('sujets')
        expire = request.POST.get('expire')

        video = Videos(
            video=video,
            titre=titre,
            description=description,
            sujets=sujets,
            expire=expire,

        )
        video.save()
        messages.success(request, 'successufully added ')
        return redirect('view_video')
    return render(request, 'Hod/add_video.html')


@login_required(login_url='/')
def View_Video(request):
    video = Videos.objects.all()
    myFilter = VideoFilter(request.GET, queryset=video)
    video = myFilter.qs
    context = {
        'video': video,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_video.html', context)


def Delete_Video(request, id):
    video = Videos.objects.get(id=id)
    video.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_video')


@login_required(login_url='/')
def Edit_Video(request, id):
    video = Videos.objects.filter(id=id)
    context = {
        'video': video,
    }
    return render(request, 'Hod/edit_video.html', context)


def Update_Video(request):
    if request.method == "POST":
        video = request.FILES.get('video')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        sujets = request.POST.get('sujets')
        expire = request.POST.get('expire')
        video = Videos(
            video=video,
            titre=titre,
            description=description,
            sujets=sujets,
            expire=expire,
        )
        video.save()
        messages.success(request, 'successufully added ')
        return redirect('view_video')
    return render(request, 'Hod/edit_video.html')


def Add_pdf(request):
    if request.method == "POST":
        pdf = request.FILES.get('pdf')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        sujets = request.POST.get('sujets')
        expire = request.POST.get('expire')
        pdf = PDF(
            pdf=pdf,
            titre=titre,
            description=description,
            sujets=sujets,
            expire=expire,
        )
        pdf.save()
        messages.success(request, 'successufully added ')
        return redirect('view_pdf')
    return render(request, 'Hod/add_pdf.html')


@login_required(login_url='/')
def View_pdf(request):
    pdf = PDF.objects.all()
    myFilter = PdfFilter(request.GET, queryset=pdf)
    pdf = myFilter.qs
    context = {
        'pdf': pdf,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_pdf.html', context)


def Delete_pdf(request, id):
    pdf = PDF.objects.get(id=id)
    pdf.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_pdf')


@login_required(login_url='/')
def Details_pdf(request, id):
    pdf = PDF.objects.filter(id=id)

    context = {
        'pdf': pdf,
    }
    return render(request, 'Hod/details_pdf.html', context)


@login_required(login_url='/')
def Edit_pdf(request, id):
    pdf = PDF.objects.filter(id=id)
    context = {
        'pdf': pdf,
    }
    return render(request, 'Hod/edit_pdf.html', context)


def Update_pdf(request):
    if request.method == "POST":
        pdf = request.FILES.get('pdf')
        pdf_id = request.POST.get('pdf_id')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        sujets = request.POST.get('sujets')
        expire = request.POST.get('expire')
        pdf = PDF(
            pdf=pdf,
            id=pdf_id,
            titre=titre,
            description=description,
            sujets=sujets,
            expire=expire,
        )
        pdf.save()
        messages.success(request, 'successufully added ')
        return redirect('view_pdf')
    return render(request, 'Hod/add_pdf.html')


def Add_word(request):
    if request.method == "POST":
        word = request.FILES.get('word')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        nature = request.POST.get('nature')
        sujets = request.POST.get('sujets')
        expire = request.POST.get('expire')

        word = Word(
            word=word,
            titre=titre,
            description=description,
            nature=nature,
            sujets=sujets,
            expire=expire,

        )
        word.save()
        messages.success(request, 'successufully added ')
        return redirect('view_word')
    return render(request, 'Hod/add_word.html')


@login_required(login_url='/')
def View_word(request):
    word = Word.objects.all()
    myFilter = WordFilter(request.GET, queryset=word)
    word = myFilter.qs
    context = {
        'word': word,
        'myFilter': myFilter,
    }
    return render(request, 'Hod/view_word.html', context)


def Delete_word(request, id):
    word = Word.objects.get(id=id)
    word.delete()
    messages.success(request, 'Successufully Deleted')
    return redirect('view_word')


@login_required(login_url='/')
def Edit_word(request, id):
    word = Word.objects.filter(id=id)
    context = {
        'word': word,
    }
    return render(request, 'Hod/edit_word.html', context)


def Update_word(request):
    if request.method == "POST":
        word = request.FILES.get('word')
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        nature = request.POST.get('nature')
        sujets = request.POST.get('sujets')
        expire = request.POST.get('expire')
        word = Word(
            word=word,
            titre=titre,
            description=description,
            nature=nature,
            sujets=sujets,
            expire=expire,
        )
        word.save()
        messages.success(request, 'successufully added ')
        return redirect('view_word')
    return render(request, 'Hod/edit_word.html')


def  View_Stock(request):
    article = Article.objects.all()

    context={
        'article':article,
    }
    return render (request,'Hod/view_stock.html',context)


def Print_Article(request,id):
    return render (request,'Hod/print_article.html')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'Hod/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        a = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_ged = a.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_ged)
        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):

    month = 'month=' + str(d.year) + '-' + str(d.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()
def get_object_or_404(Event, pk):
    pass


def event(request):
    return render(request, 'Hod/event.html')

def Add_Unite(request):
    if request.method == "POST":
        name = request.POST.get('name')
        unite = Unite(
            name=name,
        )
        unite.save()
        messages.success(request, 'successufully added ')
        return redirect('add_article')
    return(request,'Hod/add_article.html')

def Chartjs(request):
    fournisseurs_count = Fournisseur.objects.all().count()
    client_count = Client.objects.all().count()
    article = Article.objects.all().count()

    image = FichierDoc.objects.all().count()
    video = Videos.objects.all().count()
    word = Word.objects.all().count()
    pdf = PDF.objects.all().count()

    user_femme=Staff.objects.filter(gender="Femme").count()
    user_homme=Staff.objects.filter(gender="Homme").count()
    commande_count=Commande.objects.count()
    commande=Commande.objects.all()

    context={
        'fournisseurs_count':fournisseurs_count,
        'client_count':client_count,
        'article':article,
        'image':image,
        'video':video,
        'commande':commande,
        'word':word,
        'pdf':pdf,
        'user_femme':user_femme,
        'user_homme':user_homme,
        'commande_count':commande_count,
    }
    return render(request,'Hod/chartjs.html',context)