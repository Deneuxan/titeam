from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import InscriptionForm, ConnexionForm, ProfileForm
from carGeneration.models import Utilisateur, Module, Siege, Coque

import hashlib
from . import tools
from .tools import is_loged, login, logout


# Create your views here.

def accueil(request) :

	try:
		Module(nom="Télévision", description="Ecran plat full HD, une qualité de son et d'image incroyable", prix=15).save()
		Module(nom="Minibar", description="En cas de mini soif", prix=5).save()
		Module(nom="Maxibar", description="En cas de maxi soif", prix=10).save()
		Module(nom="Chaine Hifi", description="Système HiFi tout-en-un avec amplificateur stéréo DAC intégré MyAMPPaire d'enceintes Chorus 706 - 2 voies Bass reflexPuissance 2 x 60 Watts sous 4 ohms - Technologie Bluetooth aptX Entrées numériques et analogiques - Port USB et sortie Casque - Câbles enceintes inclus", prix=15).save()
		Module(nom="Console", description="Au choix parmi Playstation 7, Xbox Y, Switch 4 et game boy advance 3D. Fourni avec câble, manette et télévision", prix=60).save()
		Module(nom="Tireuse à bière", description="Un incontournable parmi les incontournables des modules proposés", prix=9).save()
		Module(nom="Bureau", description="Bureau ergonomique et optimiser pour rattraper le travail en retard sur la route", prix=10).save()
		Module(nom="Vidéoconference", description="Kit de videoconference, casque audio, micro et projecteur", prix=10).save()
		Module(nom="Salle maquillage", description="Lavabo et classiques du maquillage", prix=9).save()
		Module(nom="Four", description="Un four est une enceinte maçonnée ou un appareil, muni d'un système de chauffage puissant, qui transforme, par la chaleur, les produits et les objets", prix=10).save()
		Module(nom="Micro ondes", description="L'alternative au four", prix=10).save()
		Module(nom="Aquarium", description="Petit aquarium, eau douce, différentes varietés de petits poisson tels que truites et autres salmonidés. Très intéressant en combinaison avec le four.", prix=20).save()
		Module(nom="Karaoké", description="Sélection de titres populaires : Les lacs du connemara, la traviata...", prix=10).save()

		Siege(nom="Siege", description="Siege de base", prix=5).save()
		Siege(nom="Siege luxe", description="Siege automassant possibilité de passer en couchette", prix=15).save()


		Coque(nom="Vitrage", description="Vitrage classique", prix=5).save()
		Coque(nom="Vitrage electrochrome", description="vitrage personnalisable, possibilité de choisir la teinte", prix=15).save()
	except:
		pass


	return HttpResponse("Accueil")

def inscription(request):
	if is_loged(request) :
		return redirect('accueil')

	form = InscriptionForm(request.POST or None)

	if form.is_valid(): 
		envoi = True
		pseudo = form.cleaned_data['pseudo']
		mail = form.cleaned_data['mail']
		mdp = hashlib.sha256(form.cleaned_data['mdp'].encode()).hexdigest()     
		usr = Utilisateur(pseudo = pseudo, mail = mail, mdp = mdp)
		# print(usr.mdp)
		usr.save()
		return redirect('connexion')
	
	return render(request, 'carGeneration/inscription.html', locals())


def connexion(request):
	if is_loged(request) :
		return redirect('accueil')

	form = ConnexionForm(request.POST or None)

	string = ""
	if form.is_valid():
		pseudo = form.cleaned_data['pseudo']
		mdp = form.cleaned_data['mdp']
		if login(request, pseudo, mdp) :
			return redirect('accueil')
	return render(request, 'carGeneration/connexion.html', locals())

def deconnexion(request):
	logout(request)
	return redirect('connexion')


def desinscription(request):
	if is_loged(request):
		user = Utilisateur.objects.get(pseudo=request.session['username'])
		logout(request)
		user.delete()
	return redirect('connexion')

def creationProfile(request):
	form = ProfileForm(request.POST or None)

	if form.is_valid(): 
		# envoi = True
		# pseudo = form.cleaned_data['pseudo']
		# mail = form.cleaned_data['mail']
		# mdp = hashlib.sha256(form.cleaned_data['mdp'].encode())      
		# usr = Utilisateur(pseudo = pseudo, mail = mail, mdp = mdp)
		# print(usr.mdp)
		# usr.save()
		return HttpResponse("bien ouej")
	
	return render(request, 'carGeneration/creationProfile.html', locals())




def createSchedul(request):
	return HttpResponse("Cocuou")
