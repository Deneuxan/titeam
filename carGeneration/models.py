from django.db import models

# Create your models here.

class Module(models.Model):
	nom = models.CharField(max_length=50, unique=True)
	description = models.TextField(max_length=255, null = True)
	prix = models.FloatField()

	def __str__(self):
		return self.nom

class Siege(models.Model):
	nom = models.CharField(max_length=50, unique=True)
	description = models.TextField(max_length=255, null = True)
	prix = models.FloatField()

	def __str__(self):
		return self.nom


class Coque(models.Model):
	nom = models.CharField(max_length=50, unique=True)
	description = models.TextField(max_length=255, null = True)
	prix = models.FloatField()

	def __str__(self):
		return self.nom
		
class Profil(models.Model):
	module1 = models.ForeignKey(Module, related_name='option1', null = True)
	module2 = models.ForeignKey(Module, related_name='option2', null = True)
	module3 = models.ForeignKey(Module, related_name='option3', null = True)
	module4 = models.ForeignKey(Module, related_name='option4', null = True)


	siege1 = models.ForeignKey(Siege, related_name='siege1')
	siege2 = models.ForeignKey(Siege, related_name='siege2', null = True)
	siege3 = models.ForeignKey(Siege, related_name='siege3', null = True)
	siege4 = models.ForeignKey(Siege, related_name='siege4', null = True)

	coque = models.ForeignKey(Coque)

	def __str__(self):
		return self


class Utilisateur(models.Model):
	pseudo = models.CharField(max_length=25, unique=True)
	mail = models.EmailField(max_length=50, unique=True)
	mdp = models.CharField(max_length=50)

	profils = models.ManyToManyField(Profil, through='NomProfil')

	def __str__(self):
		return self.pseudo


class NomProfil(models.Model):
	nom = models.CharField(max_length=50, unique= True)

	utilisateur = models.ForeignKey(Utilisateur)
	profil = models.ForeignKey(Profil)

	def __str__(self):
		return "{0}.{1}".format(self.utilisateur, self.nom)


class Reservation(models.Model):
	date = models.DateTimeField(auto_now_add = False, auto_now = False)
	duration =  models.IntegerField()
	prix = models.FloatField()
	utilisateur = models.ForeignKey(Utilisateur)

	def __str__(self):
		return "{0}.{1}.{2}".format(self.date,self.duration,self.prix)

