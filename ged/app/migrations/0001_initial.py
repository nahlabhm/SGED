# Generated by Django 3.2.15 on 2022-11-22 19:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'STAFF')], default=1, max_length=50)),
                ('profile_pic', models.ImageField(upload_to='profile_pic')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('cump', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100)),
                ('parcourrir', models.ImageField(upload_to='parcourrir')),
                ('prix_ht', models.CharField(max_length=100, null=True)),
                ('Quantite', models.CharField(max_length=100)),
                ('prix_a', models.CharField(max_length=100)),
                ('prix_v', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
                ('date_c', models.CharField(max_length=100)),
                ('date_r', models.CharField(max_length=100)),
                ('paiement', models.CharField(max_length=100)),
                ('remise', models.CharField(max_length=100)),
                ('tva', models.CharField(max_length=100)),
                ('ttc', models.CharField(max_length=100)),
                ('Quantite', models.CharField(max_length=100)),
                ('prix_a', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.article')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('date_f', models.CharField(max_length=100)),
                ('date_e', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FichierDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sujets', models.CharField(max_length=100)),
                ('nature', models.CharField(max_length=100)),
                ('couverture', models.CharField(max_length=100)),
                ('expire', models.CharField(max_length=100)),
                ('contenu', models.ImageField(upload_to='contenu')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
                ('photo', models.ImageField(upload_to='photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sujets', models.CharField(max_length=100)),
                ('couverture', models.CharField(max_length=100)),
                ('expire', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='pdf/%y')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('document', models.ImageField(upload_to='document')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sujets', models.CharField(max_length=100)),
                ('couverture', models.CharField(max_length=100)),
                ('expire', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video/%y')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sujets', models.CharField(max_length=100)),
                ('nature', models.CharField(max_length=100)),
                ('expire', models.CharField(max_length=100)),
                ('word', models.FileField(upload_to='word/%y')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.article')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('services_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.services')),
            ],
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('date', models.CharField(max_length=100, null=True)),
                ('actuelle', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('article_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.article')),
                ('commande_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.commande')),
            ],
        ),
        migrations.CreateModel(
            name='PaiementFournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('date_paiement', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100, null=True)),
                ('montant', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('facture_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.facture')),
            ],
        ),
        migrations.AddField(
            model_name='facture',
            name='reception_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.reception'),
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
                ('date_devis', models.CharField(max_length=100)),
                ('validite_devis', models.CharField(max_length=100)),
                ('paiement', models.CharField(max_length=100)),
                ('remise', models.CharField(max_length=100)),
                ('tva', models.CharField(max_length=100)),
                ('ttc', models.CharField(max_length=100)),
                ('Quantite', models.CharField(max_length=100)),
                ('prix_vente', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.article')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.client')),
                ('unite_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.unite')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='fournisseur_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.fournisseur'),
        ),
        migrations.AddField(
            model_name='commande',
            name='unite_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.unite'),
        ),
        migrations.AddField(
            model_name='article',
            name='unite_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.unite'),
        ),
    ]
