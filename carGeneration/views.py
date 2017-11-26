from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import InscriptionForm, ConnexionForm, ProfileForm
from carGeneration.models import Utilisateur

import hashlib
from . import tools
from .tools import is_loged, login, logout


# Create your views here.

def accueil(request) :
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




