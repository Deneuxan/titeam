from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import InscriptionForm, ConnexionForm, ProfileForm
from carGeneration.models import Utilisateur

import hashlib

# Create your views here.

def inscription(request):
	form = InscriptionForm(request.POST or None)

	if form.is_valid(): 
		envoi = True
		pseudo = form.cleaned_data['pseudo']
		mail = form.cleaned_data['mail']
		mdp = hashlib.sha256(form.cleaned_data['mdp'].encode())      
		usr = Utilisateur(pseudo = pseudo, mail = mail, mdp = mdp)
		# print(usr.mdp)
		# usr.save()
		return redirect('connexion')
	
	return render(request, 'carGeneration/inscription.html', locals())


def connexion(request):
	# ici le code
	string = ""
	for ut in Utilisateur.objects.all():
		string += ut.pseudo
		string += " -- "

	return HttpResponse(string)

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




