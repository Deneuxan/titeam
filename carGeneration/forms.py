from django import forms
from .models import Utilisateur

class InscriptionForm(forms.Form):

	pseudo = forms.CharField(max_length=25,required=True)
	mail = forms.EmailField(max_length=50,label="Votre adresse mail",required=True)
	mdp = forms.CharField(max_length=50,widget=forms.PasswordInput,required=True)

	def clean_pseudo(self):
		pseudo = pseudo=self.cleaned_data['pseudo']
		if Utilisateur.objects.filter(pseudo=pseudo):
			raise forms.ValidationError("Ce pseudo est déjà pris !")

		return pseudo
    

class ConnexionForm(forms.Form):
	pseudo = forms.CharField(max_length=25,required=True)
	mdp = forms.CharField(max_length=50, widget=forms.PasswordInput,required=True)
