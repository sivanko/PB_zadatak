from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext, loader
from evidencijatroskova.models import Troskovi, Evidencija
from urllib.request import urlopen
import json
import decimal
from django.db.models import Sum
from datetime import datetime


# Create your views here.

def index(request):
    print('nesto')


def insert_zapisa(request):
    context = RequestContext (request)
    izbornik = []
    vrstatroska = Troskovi.objects.filter(tro_aktivan='X')
    izbor = ('---','---')
    izbornik.append(izbor)
    for VT in vrstatroska:
        pomocni = (VT.tro_id, VT.tro_opis)
        izbornik.append(pomocni)

    if request.method == 'POST':
        print(request.POST['iznos'])
        transakcija = Troskovi.objects.filter(tro_id=request.POST['vrsta'])
        zapis = Evidencija()
        zapis.ev_datum = request.POST['datum']
        if transakcija[0].tro_vrsta == 'P':
            zapis.ev_iznos = -1 * decimal.Decimal(request.POST['iznos'])
        else:
            zapis.ev_iznos = request.POST['iznos']
        zapis.ev_vrsta = Troskovi.objects.get(tro_id=request.POST['vrsta'])
        zapis.ev_valuta = request.POST['valuta']
        zapis.ev_korisnik = request.POST['korisnik']
        zapis.ev_opis = request.POST['opis']
        try:
            print(zapis.ev_iznos)
            zapis.save()
        except Exception as e:
            print(e)
            return render(request, 'evidencijatroskova/greska.html')
        return render(request, 'evidencijatroskova/unos_troska.html', {'izbornik': izbornik})
    else:
        return render(request, 'evidencijatroskova/unos_troska.html', {'izbornik': izbornik})

def pregled_zapisa(request):
    context = RequestContext (request)
    if request.method == 'POST':
        if request.POST['sortiranje'] == 'DSC':
            sortiranje = '-ev_datum'
        else:
            sortiranje = 'ev_datum'
        #broj_zapisa = request.POST['broj_zapisa']
        rezultat = Evidencija.objects.filter().order_by(sortiranje)
        print(rezultat)
        return render(request, 'evidencijatroskova/pregled_zapisa.html', {'zapisi': rezultat})
    else:
        return render(request, 'evidencijatroskova/pregled_zapisa.html')

def pregled_ukupno(request):
    context = RequestContext (request)
    danas = datetime.now().date()
    distinct_valute = Evidencija.objects.values('ev_valuta').distinct()
    ukupni_iznos = 0
    specifikacija = []
    for valuta in distinct_valute:
        suma = Evidencija.objects.filter(ev_valuta=valuta['ev_valuta']).aggregate(Sum('ev_iznos'))
        
        if valuta['ev_valuta'] == 'HRK':
            tecaj = 1
            iznos = suma['ev_iznos__sum']
        else:
            tecaj = dohvat_tecaja(valuta['ev_valuta'], danas)
            iznos = suma['ev_iznos__sum'] * tecaj
        pomocni = (valuta['ev_valuta'],round(suma['ev_iznos__sum'],2), tecaj, round(iznos, 2))
        specifikacija.append(pomocni)
        ukupni_iznos = ukupni_iznos + round(iznos, 2)
        datum = danas.strftime("%d.%m.%Y")
    return render(request, 'evidencijatroskova/stanje_na_dan.html', {'specifikacija': specifikacija, 'iznos': ukupni_iznos, 'datum': datum})


def pregled_specifikacija(request):
    context = RequestContext (request)
    specifikacija = []
    distinct_valute = Evidencija.objects.values('ev_valuta').distinct()
    for valuta in distinct_valute:
        distinct_transakcija = Evidencija.objects.filter(ev_valuta=valuta['ev_valuta']).values('ev_vrsta').distinct()
        for trx in distinct_transakcija:
            suma_trx = Evidencija.objects.filter(ev_valuta=valuta['ev_valuta'], ev_vrsta=trx['ev_vrsta']).aggregate(Sum('ev_iznos'))
            opis = Troskovi.objects.filter(tro_id=trx['ev_vrsta'])[0].tro_opis
            pomocni = (opis, valuta['ev_valuta'], round(suma_trx['ev_iznos__sum'], 2))
            specifikacija.append(pomocni)
        suma = Evidencija.objects.filter(ev_valuta=valuta['ev_valuta']).aggregate(Sum('ev_iznos'))
        pomocni = ('Ukupno', valuta['ev_valuta'], round(suma['ev_iznos__sum'], 2))
        specifikacija.append(pomocni)
    return render(request, 'evidencijatroskova/stanje_specifikacija.html', {'specifikacija': specifikacija})

def dohvat_tecaja(valuta, datum):
    url = 'https://api.hnb.hr/tecajn/v1?datum={}&valuta={}'.format(datum, valuta)
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    html_dict = json.loads(html)
    return decimal.Decimal(html_dict[0]['Srednji za devize'].replace(',','.'))



    




            

