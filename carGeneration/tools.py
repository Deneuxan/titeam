from .models import Utilisateur
import hashlib

def is_loged(request):
	if request.session.has_key('username'):
		return True
	return False

def login(request, pseudo, mdp):
	if not is_loged(request) :
		mdp_encoded = hashlib.sha256(mdp.encode())    
		try:
			user = Utilisateur.objects.get(pseudo=pseudo)

			if user.mdp == mdp_encoded.hexdigest() :
				request.session['username'] = pseudo
				return True

		except Utilisateur.DoesNotExist:
			return False
	return False


def logout(request):
	if is_loged(request) :
		try:
			del request.session['username']
			return True
		except:
			return False