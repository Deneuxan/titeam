from django import forms

class InscriptionForm(forms.Form):

	pseudo = forms.CharField(max_length=25,required=True)
	mail = forms.EmailField(label="Votre adresse mail",required=True)
	mdp = forms.CharField(widget=forms.PasswordInput,required=True)
    
