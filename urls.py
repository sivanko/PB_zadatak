from django.conf.urls import url, include
from evidencijatroskova import views

app_name = 'evidencijatroskova'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^unos$', views.insert_zapisa, name='Unos zapisa'),
	url(r'^unos/$', views.insert_zapisa, name='Unos zapisa'),
	url(r'^pregled$', views.pregled_zapisa, name='Pregled zapisa'),
	url(r'^pregled/$', views.pregled_zapisa, name='Pregled zapisa'),
	url(r'^stanja$', views.pregled_specifikacija, name='Pregled stanja valuta'),
	url(r'^stanja/$', views.pregled_specifikacija, name='Pregled stanja_valuta'),
	url(r'^stanja_danas$', views.pregled_ukupno, name='Pregled stanja danas'),
	url(r'^stanja_danas/$', views.pregled_ukupno, name='Pregled stanja danas'),
]
