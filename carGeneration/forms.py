from django import forms
from .models import Utilisateur
from .models import Profil

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


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profil

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['module1'].widget.attrs.update({'class' : 'validate'})