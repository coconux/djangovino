from django.db import models
import re
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MaxLengthValidator

from django.contrib.auth.models import User

from django.forms import ModelForm
from django import forms
# Create your models here.


class Cave(models.Model):

    user = models.ForeignKey(User, related_name='monProprio')
    nom = models.CharField(default="Ma cave",max_length=500, help_text="")
    lieu = models.CharField(default="Ma cave",max_length=500, help_text="")
    lignes = models.IntegerField(default=3,help_text="Nombre de ligne de\
                                 votre cave")
    colonnes = models.IntegerField(default=3,help_text="Nombre de colonne de\
                                 votre cave")

    dateCreation = models.DateTimeField(auto_now_add=True, help_text="")
    dateModification = models.DateTimeField(auto_now=True, help_text="")

    # Avant de sauvegarder une cave, nous créons les cellules si celles-ci n'hesitent pas
    def save(self, *args, **kwargs):
        super(Cave, self).save(*args, **kwargs) # Appeler la "vraie" méthode save().
        #Creer les cellules
        A =[(x, y)  for y in [yy for yy in range (0,self.lignes,1)] for x in [xx for xx in range(0,self.colonnes,1)]  ]
        [ Cellule.objects.get_or_create(cave=self,x=A[X][0],y=A[X][1], defaults={'cave':self,'x':A[X][0],'y':A[X][1]})  for X in range (0,len(A),1)]
        #do_something_else()

    # Retourne la capacite de la cave
    @property
    def capacite(self):
        return self.lignes * self.colonnes

    # Retourne le nombre d'emplacement libre dans la cave
    @property
    def emplacementLibre(self):
        occ = sum([b.occupe is True for b in self.mesCellules.select_related()])
        return self.capacite - occ

    # Retourne le nombre d'emplacement occupe dans la cave
    @property
    def emplacementOccupe(self):
        occ = sum([b.occupe is True for b in self.mesCellules.select_related()])
        return  occ

    # Retourne le % d'occupation de la cave
    @property
    def pourcentOcc(self):
        a = self.emplacementOccupe * 100 /self.capacite
        return  a

    # Retourne le % libre de la cave
    @property
    def pourcentLibre(self):
        a = self.emplacementLibre* 100 /self.capacite
        return  a

    #Retourne un dictionnaire
    @property
    def pourcentCouleur(self):
        cellOcc=[b for b in self.mesCellules.select_related() if b.occupe is True]
        listeCouleur=[b.maBouteille.refB.couleurB.nom for b in cellOcc]
        listePourcent=dict((i,listeCouleur.count(i)/self.capacite*100) for i in listeCouleur)
        return listePourcent

    #Retourne le volume en Ml contenu dans la cave
    @property
    def volumeCave(self):
        cellOcc=[b for b in self.mesCellules.select_related() if b.occupe is True]
        a = sum([b.maBouteille.refB.typeB.ml for b in cellOcc])
        return  a

    #Retourne la valeur en Euros de la cave
    @property
    def valeurCave(self):
        cellOcc=[b for b in self.mesCellules.select_related() if b.occupe is True]
        listePrix = [b.maBouteille.prixB for b in cellOcc]
        if listePrix:
            a = {'min': min(listePrix), 'max': max(listePrix), 'total':sum(listePrix)}
        else:
            a = {'min': '-', 'max': '-', 'total':'-'}
        return  a

    #Retourne la valeur en Euros de la cave
    @property
    def anneeCave(self):
        cellOcc=[b for b in self.mesCellules.select_related() if b.occupe is True]
        listeAnnee = [b.maBouteille.refB.anneeB.annee.year for b in cellOcc]
        if listeAnnee:
            a = {'min': min(listeAnnee), 'max': max(listeAnnee)}
        else:
            a = {'min': '-', 'max': '-'}

        return a




    def __str__(self):
        return '%s' %self.nom


class Cellule(models.Model):
    cave = models.ForeignKey('Cave', related_name='mesCellules' ,help_text="la cave possedant cette cellule", blank=True, null=True, on_delete=models.CASCADE)
    x = models.IntegerField(default=3,help_text="Nombre de ligne de\
                                 votre cave")
    y = models.IntegerField(default=3,help_text="Nombre de colonne de\
                                 votre cave")

    # Retourne la bouteille dans la cellule ou None (idem self.maBouteille)
    @property
    def occupeBy(self):
        try:
            occupeBy = type(self.maBouteille)
        except ObjectDoesNotExist:
            occupeBy = None
        return occupeBy

    # Retourne True si la cellule est occupe par une bouteille             
    @property
    def occupe(self):
        if self.occupeBy is None:
            occupe = False
        else:
            occupe = True
        return occupe


    def __str__(self):
        return '%s --> %s;%s -->%s -->%s' %(self.cave.nom, self.x, self.y,self.occupe,self.occupeBy)

class RefBouteille(models.Model):

    def upload_path(self, filename):
            #return 'imgVin/%s_%s' % (self.nomB.replace(" ","_"), filename)
            return 'imgVin/%s_%s.%s' % (self.pk, "bouteille", filename.rsplit('.')[-1])

    nomB = models.CharField(default="Ma teille",max_length=50, help_text="")
    typeB = models.ForeignKey('TypeBouteille', help_text="le type de\
                              bouteille", blank=True, null=True, on_delete=models.SET_NULL)
    couleurB = models.ForeignKey('Couleur', help_text="la couleur du vin",\
                               blank=True, null=True, on_delete=models.SET_NULL)

    classificationB = models.ForeignKey('Classification', help_text="la classif du vin",\
                               blank=True, null=True, on_delete=models.SET_NULL)

    anneeB = models.ForeignKey('Annee', related_name='creation', help_text="l'année du vin",\
                               blank=True, null=True, on_delete=models.SET_NULL)

    regionB = models.ForeignKey('Region', blank=True ,null=True, on_delete=models.SET_NULL)

    imageB = models.FileField(default="void.jpeg",upload_to=upload_path )

    def __str__(self):
        return '%s' %self.nomB

    # Retourne un motif concatenant les infos pour la recherche sur plusieurs champs
    @property
    def motif(self):

        return str(self.anneeB.nom)+' '+str(self.nomB)+' '+str(self.typeB.nom)



class Bouteille(models.Model):

    user = models.ForeignKey(User, related_name='monProprioBouteille')

    refB = models.ForeignKey('RefBouteille', related_name='maReference', help_text="la reference bouteille" )

    gardeMinB = models.ForeignKey('Annee', related_name='consoMin', help_text="Annee minimale pour boire la bouteille",\
                               blank=True, null=True, on_delete=models.SET_NULL)
    gardeMaxB = models.ForeignKey('Annee', related_name='consoMax', help_text="Annee max pour boire la bouteille",\
                               blank=True, null=True, on_delete=models.SET_NULL)
    prixB = models.DecimalField(default="",max_digits=8,decimal_places=2, help_text="Prix de la bouteille en euros €")

    celluleB = models.OneToOneField('Cellule', related_name='maBouteille', primary_key=False, blank=True ,null=True)

    rating = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(5)])

    bu = models.BooleanField(help_text="Cocher si vous avez bu cette bouteille")
    commentaireBu = models.TextField(default="", blank=True, max_length=750,validators=[MaxLengthValidator(750)])
    partageCommentaireBu = models.BooleanField(help_text="Rendre ce commentaire visible par tous les membres")

    cadeau = models.BooleanField(help_text="Vous as-t'on offert cette bouteille ")
    commentaireCadeau = models.TextField(default="", blank=True, max_length=750,validators=[MaxLengthValidator(750)])

    offert = models.BooleanField(help_text="Avez-vous offert cette bouteille ")
    commentaireOffert = models.TextField(default="", blank=True, max_length=750,validators=[MaxLengthValidator(750)])

    partage = models.BooleanField(help_text="Rendre cette bouteille visible par tous?")

    observation = models.TextField(default="", blank=True, max_length=750,validators=[MaxLengthValidator(750)])


    def __str__(self):
        return '%s' %self.refB.anneeB +' - %s' %self.refB.nomB


    # Sort la bouteille d'un emplacement    
    def libere(self):
        self.place(None)
        self.save()

    # Met la bouteille dans un emplacement
    def place(self,dest):
        self.celluleB = dest
        self.save()




class Annee(models.Model):
    nom = models.CharField(unique=True,default="2009",max_length=10,help_text="")
    annee = models.DateField(default="01/01/2009", help_text="")

    # Apres validation du formulaire, nous faisons quelques transformations (avant save)
    # Ex: nom = "    2009 " Resultat nom="2009" 
    def clean(self):
        self.nom = re.sub(' +',' ',self.nom).strip().title()

    def __str__(self):
        return '%s' %str(self.nom)

class Couleur(models.Model):
    nom = models.CharField(unique=True,default="Ma couleur",max_length=50, help_text="")

    def __str__(self):
        return '%s' %self.nom

    # Apres validation du formulaire, nous faisons quelques transformations (avant save)
    # Ex: nom = "    blue     ciel " Resultat nom="Bleu ciel" 
    def clean(self):
        self.nom = re.sub(' +',' ',self.nom).strip().title()

class TypeBouteille(models.Model):
    nom = models.CharField(unique=True,default="Magnum",max_length=50, help_text="")
    volume = models.CharField(default="75cl",max_length=10, help_text="")
    ml = models.DecimalField(max_digits=6,decimal_places=2, help_text="Quantité  en ml")

    def __str__(self):
        return '%s' %self.nom +' --> %s' %self.volume

    # Apres validation du formulaire, nous faisons quelques transformations (avant save)
    # Ex: nom = "    blue     ciel " Resultat nom="Bleu ciel" 
    def clean(self):
        self.nom = re.sub(' +',' ',self.nom).strip().title()

class Classification(models.Model):
    nom = models.CharField(unique=True,default="Grand cru",max_length=100, help_text="")

    def __str__(self):
        return '%s' %self.nom

    # Apres validation du formulaire, nous faisons quelques transformations (avant save)
    # Ex: nom = "    blue     ciel " Resultat nom="Bleu ciel"
    def clean(self):
        self.nom = re.sub(' +',' ',self.nom).strip().title()

class Pays(models.Model):
    nom = models.CharField(unique=True,default="France",max_length=100, help_text="")

    def __str__(self):
        return '%s' %self.nom

    # Apres validation du formulaire, nous faisons quelques transformations (avant save)
    # Ex: nom = "    blue     ciel " Resultat nom="Bleu ciel"
    def clean(self):
        self.nom = re.sub(' +',' ',self.nom).strip().title()

class Region(models.Model):
    paysR = models.ForeignKey('Pays',  null=False, on_delete=models.CASCADE)
    nom = models.CharField(unique=True,default="Bordeaux",max_length=100, help_text="")

    def __str__(self):
        return '%s' %self.nom



""" A la fin """
class BouteilleForm(ModelForm):
    class Meta:
        model = Bouteille
        #Apres le syncdb, avec postgres
        #widgets = {'commentaireBu': forms.HiddenInput(), 'commentaireCadeau': forms.HiddenInput(),'commentaireOffert': forms.HiddenInput()}

        fields = ['refB', 'prixB', 'gardeMinB', 'gardeMaxB','bu','commentaireBu','partageCommentaireBu','cadeau', 'commentaireCadeau', 'offert','commentaireOffert','observation','partage']

        #fields = ['refB', 'prixB', 'gardeMinB', 'gardeMaxB','observation']
        exclude = ['user']

