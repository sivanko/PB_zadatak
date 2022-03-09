from django.db import models

# Create your models here.

class Troskovi(models.Model):
    tro_id = models.AutoField(primary_key=True, verbose_name='Primarni kljuc tablice')
    tro_vrsta = models.CharField('Vrsta transakcije, D - uplata, P - isplata', max_length=1, null=False)
    tro_opis = models.CharField('opis troska', max_length=30, null=False)
    tro_aktivan = models.CharField('Flag da li je trosak aktivan ili ne', null=False, default='X', max_length=1)
    def __str__(self):
        return self.tro_opis
    @property
    def trosak(self):
        return self.tro_opis
    

class Evidencija(models.Model):
    ev_id = models.AutoField(primary_key=True, verbose_name='Primarni kljuc tablice')
    ev_datum = models.DateField('Datum transakcije',null=False)
    ev_iznos = models.DecimalField('Iznos transakcije', max_digits=13, decimal_places=2, null=False)
    ev_valuta = models.CharField('Valuta transakcije', max_length=3, null=False)
    ev_vrsta = models.ForeignKey(Troskovi, related_name='%(class)s_id', on_delete=models.CASCADE)
    ev_korisnik = models.CharField('Osoba koje je napravila transakciju', max_length=30, null=False)
    ev_opis = models.CharField('Opis transakcije', max_length=50, null=True)
    ev_vrijemeunosa = models.DateTimeField('vrijeem unosa zapisa', auto_now_add=True)


