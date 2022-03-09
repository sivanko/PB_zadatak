# Generated by Django 3.2.7 on 2022-03-08 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Troskovi',
            fields=[
                ('tro_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Primarni kljuc tablice')),
                ('tro_vrsta', models.CharField(max_length=1, verbose_name='Vrsta transakcije, D - uplata, P - isplata')),
                ('tro_opis', models.CharField(max_length=30, verbose_name='opis troska')),
                ('tro_aktivan', models.CharField(default='X', max_length=1, verbose_name='Flag da li je trosak aktivan ili ne')),
            ],
        ),
        migrations.CreateModel(
            name='Evidencija',
            fields=[
                ('ev_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Primarni kljuc tablice')),
                ('ev_datum', models.DateField(verbose_name='Datum transakcije')),
                ('ev_iznos', models.DecimalField(decimal_places=2, max_digits=13, verbose_name='Iznos transakcije')),
                ('ev_valuta', models.CharField(max_length=3, verbose_name='Valuta transakcije')),
                ('ev_korisnik', models.CharField(max_length=30, verbose_name='Osoba koje je napravila transakciju')),
                ('ev_opis', models.CharField(max_length=50, null=True, verbose_name='Opis transakcije')),
                ('ev_vrijemeunosa', models.DateTimeField(auto_now_add=True, verbose_name='vrijeem unosa zapisa')),
                ('ev_vrsta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidencija_id', to='evidencijatroskova.troskovi')),
            ],
        ),
    ]