
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,Staff_View


urlpatterns = [

                  path('home', views.homePage),
                  path('', views.Login, name='login'),
                  path('doLogin', views.doLogin, name='doLogin'),
                  path('doLogout', views.doLogout, name='logout'),
                  path('Profile', views.Profile, name='profile'),
                  path('Profile/update', views.Profile_Update, name='profile_update'),

                  path('Hod/Home', Hod_Views.Home, name='hod_home'),


                  path('Hod/user/Add', Hod_Views.Add_User, name='add_user'),
                  path('Hod/user/View', Hod_Views.View_User, name='view_user'),
                  path('Hod/user/Delete/<str:admin>', Hod_Views.Delete_User, name='delete_user'),
                  path('Hod/user/Edit/<str:id>', Hod_Views.Edit_User, name='edit_user'),
                  path('Hod/user/Update', Hod_Views.Update_User, name='update_user'),

                  path('Hod/client/Add', Hod_Views.Add_Client, name='add_client'),
                  path('Hod/client/View', Hod_Views.View_Client, name='view_client'),
                  path('Hod/client/Delete/<str:id>', Hod_Views.Delete_Client, name='delete_client'),
                  path('Hod/client/Edit/<str:id>', Hod_Views.Edit_Client, name='edit_client'),
                  path('Hod/client/Update', Hod_Views.Update_Client, name='update_client'),
                  path('Hod/client/Export', Hod_Views.Export_Excel, name='export_excel'),

                  path('Hod/fournisseur/Add', Hod_Views.Add_Fournisseur, name='add_fournisseur'),
                  path('Hod/fournisseur/View', Hod_Views.View_Fournisseur, name='view_fournisseur'),
                  path('Hod/fournisseur/Delete/<str:id>', Hod_Views.Delete_Fournisseur, name='delete_fournisseur'),
                  path('Hod/fournisseur/Edit/<str:id>', Hod_Views.Edit_Fournisseur, name='edit_fournisseur'),
                  path('Hod/fournisseur/Update', Hod_Views.Update_Fournisseur, name='update_fournisseur'),


                  path('Hod/Article/Add', Hod_Views.Add_Article, name='add_article'),
                  path('Hod/Article/View', Hod_Views.View_Article, name='view_article'),
                  path('Hod/Article/Delete/<str:id>', Hod_Views.Delete_Article, name='delete_article'),
                  path('Hod/Article/Edit/<str:id>', Hod_Views.Edit_Article, name='edit_article'),
                  path('Hod/Article/Update', Hod_Views.Update_Article, name='update_article'),
                  path('Hod/Article/details/<str:id>', Hod_Views.Voir_Article, name='voir_article'),
                  path('Hod/Article/print', Hod_Views.Print_Article, name='print_article'),
                  path('Hod/unite/Add', Hod_Views.Add_Unite, name='add_unite'),

                  path('Hod/achat/commande/Add', Hod_Views.Add_Commande, name='add_commande'),
                  path('Hod/achat/commande/View', Hod_Views.View_Commande, name='view_commande'),
                  path('Hod/achat/commande/Delete/<str:id>', Hod_Views.Delete_Commande, name='delete_commande'),
                  path('Hod/achat/commande/Edit/<str:id>', Hod_Views.Edit_Commande, name='edit_commande'),
                  path('Hod/achat/commande/Update', Hod_Views.Update_Commande, name='update_commande'),
                  path('Hod/achat/commande/details/<str:id>', Hod_Views.Voir_Commande, name='voir_commande'),

                  path('Hod/achat/reception/Add', Hod_Views.Add_Reception, name='add_reception'),
                  path('Hod/achat/reception/Add/<str:id>', Hod_Views.Add_Reception_c, name='add_reception_c'),
                  path('Hod/achat/reception/View', Hod_Views.View_Reception, name='view_reception'),
                  path('Hod/achat/reception/Delete/<str:id>', Hod_Views.Delete_Reception, name='delete_reception'),
                  path('Hod/achat/reception/details/<str:id>', Hod_Views.Voir_Reception, name='voir_reception'),
                  path('Hod/achat/reception/Edit/<str:id>', Hod_Views.Edit_Reception, name='edit_reception'),
                  path('Hod/achat/reception/update', Hod_Views.Update_Reception, name='update_reception'),

                  path('Hod/achat/facture/Add/<str:id>', Hod_Views.Add_Facture_f, name='add_facture_f'),
                  path('Hod/achat/facture/Add', Hod_Views.Add_Facture, name='add_facture'),
                  path('Hod/achat/facture/View', Hod_Views.View_Facture, name='view_facture'),
                  path('Hod/achat/facture/Delete/<str:id>', Hod_Views.Delete_Facture, name='delete_facture'),
                  path('Hod/achat/facture/Edit/<str:id>', Hod_Views.Edit_Facture, name='edit_facture'),
                  path('Hod/achat/facture/update', Hod_Views.Update_Facture, name='update_facture'),
                  path('Hod/achat/facture/Details/<str:id>', Hod_Views.Details_Facture, name='Details_facture'),



                  path('Hod/ressource/image/Add', Hod_Views.Add_Fichier, name='add_fichier'),
                  path('Hod/ressource/image/View', Hod_Views.View_Fichier, name='view_fichier'),
                  path('Hod/ressource/image/details/<str:id>', Hod_Views.Voir_Fichier, name='voir_fichier'),
                  path('Hod/ressource/image/Delete/<str:id>', Hod_Views.Delete_Fichier, name='delete_fichier'),
                  path('Hod/ressource/send', Hod_Views.Send_Fichier, name='send_fichier'),
                  path('Hod/ressource/image/Edit/<str:id>', Hod_Views.Edit_Fichier, name='edit_fichier'),
                  path('Hod/ressource/image/update', Hod_Views.Update_Fichier, name='update_fichier'),

                  path('Hod/Vente/Devis/Add', Hod_Views.Add_Devis, name='add_devis'),
                  path('Hod/Vente/Devis/view', Hod_Views.View_Devis, name='view_devis'),
                  path('Hod/Vente/Devis/Delete/<str:id>', Hod_Views.Delete_Devis, name='delete_devis'),
                  path('Hod/Vente/Devis/view_devis', Hod_Views.View_Devis_V, name='view_devis_v'),
                  path('Hod/Vente/Devis/view/Delete/<str:id>', Hod_Views.Delete_Devis_v, name='delete_devis_v'),
                  path('Hod/Vente/Devis/view/Details/<str:id>', Hod_Views.Details_Devis, name='details_devis'),
                  path('Hod/Vente/Devis/Edit/<str:id>', Hod_Views.Edit_Devis, name='edit_devis'),
                  path('Hod/Vente/Devis/Update', Hod_Views.Update_Devis, name='update_devis'),

                  path('Hod/Note/add', Hod_Views.Note_Add, name='note_add'),
                  path('Hod/Note/view', Hod_Views.View_Note, name='view_note'),
                  path('Hod/Note/Delete/<str:event_id>', Hod_Views.Delete_Note, name='delete_note'),

                  path('Hod/calendar/view', Hod_Views.CalendarView.as_view(), name='calendar'),
                  path('Hod/calendar/new', Hod_Views.event, name='event_new'),
                  path('Hod/calendar/edit)', Hod_Views.event, name='event_edit'),

                  path('Hod/ressources/Video/add', Hod_Views.Add_Video, name='add_video'),
                  path('Hod/ressources/Video/view', Hod_Views.View_Video, name='view_video'),
                  path('Hod/ressources/Video/Delete/<str:id>', Hod_Views.Delete_Video, name='delete_video'),
                  path('Hod/ressources/Video/Edit/<str:id>', Hod_Views.Edit_Video, name='edit_video'),
                  path('Hod/ressources/Video/Update', Hod_Views.Update_Video, name='update_video'),

                  path('Hod/ressources/pdf/add', Hod_Views.Add_pdf, name='add_pdf'),
                  path('Hod/ressources/pdf/view', Hod_Views.View_pdf, name='view_pdf'),
                  path('Hod/ressources/pdf/Delete/<str:id>', Hod_Views.Delete_pdf, name='delete_pdf'),
                  path('Hod/ressources/pdf/details/<str:id>', Hod_Views.Details_pdf, name='details_pdf'),
                  path('Hod/ressources/pdf/Edit/<str:id>', Hod_Views.Edit_pdf, name='edit_pdf'),
                  path('Hod/ressources/pdf/update', Hod_Views.Update_pdf, name='update_pdf'),

                  path('Hod/ressources/word/add', Hod_Views.Add_word, name='add_word'),
                  path('Hod/ressources/word/view', Hod_Views.View_word, name='view_word'),
                  path('Hod/ressources/pdf/Delete/<str:id>', Hod_Views.Delete_word, name='delete_word'),
                  path('Hod/ressources/word/Edit/<str:id>', Hod_Views.Edit_word, name='edit_word'),
                  path('Hod/ressources/word/update', Hod_Views.Update_word, name='update_word'),

                  path('Hod/Stock/View', Hod_Views.View_Stock, name='view_stock'),
                  path('Hod/statique', Hod_Views.Chartjs, name='chartjs'),

                  #user
    path('User/home',Staff_View.Home,name='staff_home'),

                  path('User/client/Add', Staff_View .Add_Client, name='add_client'),
                  path('User/client/View', Staff_View.View_Client, name='view_client'),
                  path('User/client/Delete/<str:id>', Staff_View.Delete_Client, name='delete_client'),
                  path('User/client/Edit/<str:id>', Staff_View.Edit_Client, name='edit_client'),
                  path('User/client/Update', Staff_View.Update_Client, name='update_client'),
                  path('User/client/Export', Staff_View.Export_Excel, name='export_excel'),

                  path('User/fournisseur/Add', Staff_View.Add_Fournisseur, name='add_fournisseur'),
                  path('User/fournisseur/View', Staff_View.View_Fournisseur, name='view_fournisseur'),
                  path('User/fournisseur/Delete/<str:id>', Staff_View.Delete_Fournisseur, name='delete_fournisseur'),
                  path('User/fournisseur/Edit/<str:id>', Staff_View.Edit_Fournisseur, name='edit_fournisseur'),
                  path('User/fournisseur/Update', Staff_View.Update_Fournisseur, name='update_fournisseur'),

                  path('User/Article/Add',Staff_View.Add_Article, name='add_article'),
                  path('User/Article/View', Staff_View.View_Article, name='view_article'),
                  path('User/Article/Delete/<str:id>', Staff_View.Delete_Article, name='delete_article'),
                  path('User/Article/Edit/<str:id>', Staff_View.Edit_Article, name='edit_article'),
                  path('User/Article/Update', Staff_View.Update_Article, name='update_article'),
                  path('User/Article/details/<str:id>', Staff_View.Voir_Article, name='voir_article'),
                  path('User/unite/Add', Staff_View.Add_Unite, name='add_unite'),

                  path('User/achat/commande/Add', Staff_View.Add_Commande, name='add_commande'),
                  path('User/achat/commande/View', Staff_View.View_Commande, name='view_commande'),
                  path('User/achat/commande/Delete/<str:id>', Staff_View.Delete_Commande, name='delete_commande'),
                  path('User/achat/commande/Edit/<str:id>', Staff_View.Edit_Commande, name='edit_commande'),
                  path('User/achat/commande/Update', Staff_View.Update_Commande, name='update_commande'),
                  path('User/achat/commande/details/<str:id>', Staff_View.Voir_Commande, name='voir_commande'),

                  path('User/achat/reception/Add', Staff_View.Add_Reception, name='add_reception'),
                  path('User/achat/reception/Add/<str:id>', Staff_View.Add_Reception_c, name='add_reception_c'),
                  path('User/achat/reception/View', Staff_View.View_Reception, name='view_reception'),
                  path('User/achat/reception/Delete/<str:id>', Staff_View.Delete_Reception, name='delete_reception'),
                  path('User/achat/reception/details/<str:id>', Staff_View.Voir_Reception, name='voir_reception'),
                  path('User/achat/reception/Edit/<str:id>', Staff_View.Edit_Reception, name='edit_reception'),
                  path('User/achat/reception/update', Staff_View.Update_Reception, name='update_reception'),

                  path('User/achat/facture/Add/<str:id>', Staff_View.Add_Facture_f, name='add_facture_f'),
                  path('User/achat/facture/Add', Staff_View.Add_Facture, name='add_facture'),
                  path('User/achat/facture/View', Staff_View.View_Facture, name='view_facture'),
                  path('User/achat/facture/Delete/<str:id>', Staff_View.Delete_Facture, name='delete_facture'),
                  path('User/achat/facture/Edit/<str:id>', Staff_View.Edit_Facture, name='edit_facture'),
                  path('User/achat/facture/update', Staff_View.Update_Facture, name='update_facture'),
                  path('User/achat/facture/Details/<str:id>', Staff_View.Details_Facture, name='Details_facture'),

                  path('User/ressource/image/Add', Staff_View.Add_Fichier, name='add_fichier'),
                  path('User/ressource/image/View', Staff_View.View_Fichier, name='view_fichier'),
                  path('User/ressource/image/details/<str:id>', Staff_View.Voir_Fichier, name='voir_fichier'),
                  path('User/ressource/image/Delete/<str:id>', Staff_View.Delete_Fichier, name='delete_fichier'),
                  path('User/ressource/send', Staff_View.Send_Fichier, name='send_fichier'),
                  path('User/ressource/image/Edit/<str:id>', Staff_View.Edit_Fichier, name='edit_fichier'),
                  path('User/ressource/image/update', Staff_View.Update_Fichier, name='update_fichier'),

                  path('User/Vente/Devis/Add', Staff_View.Add_Devis, name='add_devis'),
                  path('User/Vente/Devis/view', Staff_View.View_Devis, name='view_devis'),
                  path('User/Vente/Devis/Delete/<str:id>', Staff_View.Delete_Devis, name='delete_devis'),
                  path('User/Vente/Devis/view_devis', Staff_View.View_Devis_V, name='view_devis_v'),
                  path('User/Vente/Devis/view/Delete/<str:id>', Staff_View.Delete_Devis_v, name='delete_devis_v'),
                  path('User/Vente/Devis/view/Details/<str:id>', Staff_View.Details_Devis, name='details_devis'),
                  path('User/Vente/Devis/Edit/<str:id>', Staff_View.Edit_Devis, name='edit_devis'),
                  path('User/Vente/Devis/Update', Staff_View.Update_Devis, name='update_devis'),

                  path('User/Note/add', Staff_View.Note_Add, name='note_add'),
                  path('User/Note/view', Staff_View.View_Note, name='view_note'),
                  path('User/Note/Delete/<str:event_id>', Staff_View.Delete_Note, name='delete_note'),

                  path('User/calendar/view', Staff_View.CalendarView.as_view(), name='calendar'),
                  path('User/calendar/new', Staff_View.event, name='event_new'),
                  path('User/calendar/edit)', Staff_View.event, name='event_edit'),

                  path('User/ressources/Video/add', Staff_View.Add_Video, name='add_video'),
                  path('User/ressources/Video/view', Staff_View.View_Video, name='view_video'),
                  path('User/ressources/Video/Delete/<str:id>', Staff_View.Delete_Video, name='delete_video'),
                  path('User/ressources/Video/Edit/<str:id>', Staff_View.Edit_Video, name='edit_video'),
                  path('User/ressources/Video/Update', Staff_View.Update_Video, name='update_video'),

                  path('User/ressources/pdf/add', Staff_View.Add_pdf, name='add_pdf'),
                  path('User/ressources/pdf/view', Staff_View.View_pdf, name='view_pdf'),
                  path('User/ressources/pdf/Delete/<str:id>', Staff_View.Delete_pdf, name='delete_pdf'),
                  path('User/ressources/pdf/details/<str:id>', Staff_View.Details_pdf, name='details_pdf'),
                  path('User/ressources/pdf/Edit/<str:id>', Staff_View.Edit_pdf, name='edit_pdf'),
                  path('User/ressources/pdf/update', Staff_View.Update_pdf, name='update_pdf'),

                  path('User/ressources/word/add', Staff_View.Add_word, name='add_word'),
                  path('User/ressources/word/view', Staff_View.View_word, name='view_word'),
                  path('User/ressources/pdf/Delete/<str:id>', Staff_View.Delete_word, name='delete_word'),
                  path('User/ressources/word/Edit/<str:id>', Staff_View.Edit_word, name='edit_word'),
                  path('User/ressources/word/update', Staff_View.Update_word, name='update_word'),

                  path('User/Stock/View', Staff_View.View_Stock, name='view_stock'),
                  path('User/statique', Staff_View.Chartjs, name='chartjs'),


                  path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
