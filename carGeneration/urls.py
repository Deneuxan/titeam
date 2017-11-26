from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^inscription$', views.inscription, name="inscription"),
	url(r'^connexion$', views.connexion),
]