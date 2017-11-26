from django.shortcuts import render
from django.http import HttpResponse
from .forms import InscriptionForm
from carGeneration.models import Utilisateur
import hashlib

# Create your views here.

def inscription(request):
	# ici le code
	# Construire le formulaire, soit avec les données postées,
	# soit vide si l'utilisateur accède pour la première fois
	# à la page.
	form = InscriptionForm(request.POST or None)

	# Nous vérifions que les données envoyées sont valides
	# Cette méthode renvoie False s'il n'y a pas de données 
	# dans le formulaire ou qu'il contient des erreurs.

	if form.is_valid(): 

		# Ici nous pouvons traiter les données du formulaire

		# Nous pourrions ici envoyer l'e-mail grâce aux données 

		# que nous venons de récupérer
		envoi = True
		pseudo = form.cleaned_data['pseudo']
		mail = form.cleaned_data['mail']
		mdp = hashlib.sha256(form.cleaned_data['mdp'].encode())      
		usr = Utilisateur(pseudo = pseudo, mail = mail, mdp = mdp)
		print(usr.mdp)
		usr.save()
	
	# Quoiqu'il arrive, on affiche la page du formulaire.

	return render(request, 'carGeneration/inscription.html', locals())


def connexion(request):
	# ici le code
	return HttpResponse("Ca va")
