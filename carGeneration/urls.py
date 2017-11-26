from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^accueil$', views.accueil, name="accueil"),

	url(r'^inscription$', views.inscription, name="inscription"),
	url(r'^desinscription$', views.desinscription, name="desinscription"),
	url(r'^connexion$', views.connexion, name="connexion"),
	url(r'^deconnexion$', views.deconnexion, name="deconnexion"),
	url(r'^creationProfile$', views.creationProfile, name="creationProfile"),

	url(r'^createSchedul$', views.createSchedul, name='createSchedul'),
]