# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response, get_object_or_404

from django.http import HttpResponse
from cave.models import Cave, Couleur,TypeBouteille,Classification,Bouteille,Annee,Cellule,Pays,Region,RefBouteille,BouteilleForm
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from django.http import Http404

from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Count

from django.contrib.auth.models import User

from cave.forms import addBouteilleForm

"""Traitement du formulaire d'ajout de bouteille
"""
### a faire verifier que anneeMax > anneeMin
### ajouter le input pour saisir el nb bouteille

def addBouteille(request):
    #On redefinit l'action pour la valeur action dans le formulaire
    actionFormAddBouteille='/cave/addBouteille/'
    user = request.user
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = BouteilleForm(request.POST)  # Nous reprenons les données
        nbBouteille = request.POST['nb']
        if nbBouteille:
            nbBouteille = int(nbBouteille)
        else:
            nbBouteille=0

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            newBouteille = form.save(commit=False)
            for nb in range(0,nbBouteille):
                print("ajout:")
                newBouteille.user = user
                newBouteille.save();
                newBouteille.pk = None

        else:
            print ("pas valide")


    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        #idBouteille = form.cleaned_data['idBouteille']
        form = BouteilleForm()  # Nous créons un formulaire vide

    return render(request,'html/cave/formAddBouteille.html',{'form': form,'actionFormAddBouteille': actionFormAddBouteille,'nbBouteille':nbBouteille, }, context_instance=RequestContext(request))
    #return HttpResponse(request)


def addBouteille2(request):

    #On redefinit l'action pour la valeur action dans le formulaire
    actionFormAddBouteille='/cave/addBouteille/'

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = addBouteilleForm(request.POST)  # Nous reprenons les données

        ### Verifier que la bouteille existe ###




        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            idBouteille = form.cleaned_data['idBouteille']
            if idBouteille:
                bouteille = RefBouteille.objects.get(pk=idBouteille)
                if bouteille:
                    pass
                else:
                    return render(request,'html/cave/formAddBouteille.html',{'form': form,'actionFormAddBouteille': actionFormAddBouteille, }, context_instance=RequestContext(request))
            # Ici nous pouvons traiter les données du formulaire
            nbBouteille = form.cleaned_data['nbBouteille']
            prixUnitaire = form.cleaned_data['prixUnitaire']
            gardeMin = form.cleaned_data['gardeMin']
            gardeMax = form.cleaned_data['gardeMax']

            #print(idBouteille+nbBouteille+prixUnitaire+gardeMax+gardeMin)

            #On creer un formulaire vide pour reset
            form = addBouteilleForm()  # Nous créons un formulaire vide

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        idBouteille = form.cleaned_data['idBouteille']
        form = addBouteilleForm()  # Nous créons un formulaire vide

    return render(request,'html/cave/formAddBouteille.html',{'form': form,'actionFormAddBouteille': actionFormAddBouteille, }, context_instance=RequestContext(request))
    #return HttpResponse(request)


class RefBouteilleList(ListView):
    model = RefBouteille
    template_name = 'html/cave/refbouteille_list.html'

class TousLesUtilisateurs(ListView):
    # Dans le template le context_object_name  "utilisateur" recupere le retour du get_queryset
   context_object_name = "utilisateur"

   #queryset = User.objects.all()
   template_name = "html/cave/tous_les_utilisateurs.html"

    #TOutes les infos que l'on souhaitent avoir dans le template doivent etre passé au context
   def get_context_data(self, **kwargs):
        # qui dit overriding, dit appel de la méthode parent...
        context = super(TousLesUtilisateurs, self).get_context_data(**kwargs)
        # et on rajoute la date du jour dans le context
        context['aujourdhui'] = datetime.now()
        context['mec'] = self.mec
        context['toto'] = self.template_name


        # le context retourner sera automatiquement injecté dans le template
        # dans la méthode render(), que vous ne voyez pas...
        return context

   def get_queryset(self):
        self.mec = get_object_or_404(User, username=self.args[0])
        #self.mec = get_object_or_404(User, username=self.request.user)
        #self.mec est un object user, le context_object_name contient aussi ce retour
        return "cool"

#[ Cellule.objects.get_or_create(cave=c,x=1,y=1, defaults={'cave':c,'x':1,'y':w[1]})  for int(w) in range (0,len(A),1)]


@login_required()
@csrf_exempt
def addToStockFromRef(request):
    user = request.user

    post = request.POST['list_bouteille']
    # le post est au format json. On le désérialize
    list_bouteille = json.loads(post)
    # on affiche chaque élément. Ici vous devez faire votre traitement, une insertion
    # en base de données par exemple
    for bouteille in list_bouteille:
        #nom = bouteille['nom']
        idRef = bouteille['idRef']
        nb = bouteille['nb']
        for i in range(0, nb):
            newB = Bouteille.objects.create(user=user, refB_id=idRef)



        print ("Placement de "+str(idRef) + "nb:"+str(nb))

    # on fait un retour au client
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    # json data est maintenant au format JSON et pret à etre envoyé au client
    return HttpResponse(json_data, mimetype="application/json")


@login_required()
def gerercave(request,num):

    user = request.user

    # on recupere la cave passe en arg
    maCave = get_object_or_404(Cave, pk=num, user=user)
    # le template herite du template home qui contient el nombre de cave
    mesCaves = Cave.objects.filter(user=user)
    nbCave = mesCaves.count()

    #Faire le filtrage des bouteilles placées dans cette cave
    #On en filtre pas par le user, la cave appartient deja a l'utilisateur
    bouteilles = Bouteille.objects.filter( Q(celluleB__cave_id=num))

    # a modifier
    #cellOcc=[b for b in maCave.mesCellules.select_related() if b.occupe is True]



    template = 'html/cave/gererCave.html'
    #monStock = RefBouteilleList()
    data = {
        'cave':maCave,
        'lignes':range(maCave.lignes),
        'colonnes':range(maCave.colonnes),
        'nbCave':nbCave,
        'mesCaves':mesCaves,
        #'cellules':cellOcc,

    }

    #return render_to_response('html/cave/voirCave.html',{'cave': c, 'bouteilles':b, 'cellules':cellOcc, 'lignes':range(c.lignes), 'colonnes':range(c.colonnes) })

    return render_to_response(template, data, context_instance = RequestContext(request))


@login_required()
def mescaves(request):
    user = request.user
    mesCaves = Cave.objects.filter(user=user)
    nbCave = mesCaves.count()

    template = 'html/cave/mesCaves.html'
    data = {
        'nbCave':nbCave,
        'mesCaves':mesCaves,
    }

    return render_to_response(template, data, context_instance = RequestContext(request))


def testcave(request):
   return render_to_response('html/cave/dnd.html')

@login_required
def home(request):

    user = request.user
    mesCaves = Cave.objects.filter(user=user)
    nbCave = mesCaves.count()
    template = 'html/cave/home.html'
    data = {
        'nbCave':nbCave,
        'mesCaves':mesCaves,
    }

    return render_to_response(template, data, context_instance=RequestContext(request))
    #return render_to_response('html/cave/base.html',"", context_instance=RequestContext(request))


@login_required
def test(request):
    return render_to_response('html/cave/test.html',"", context_instance=RequestContext(request))

#@login_required
def stock(request):

    form = BouteilleForm()
    #Lors du premier chargement de la page stock, il faut rendre le formAddBouteille.
    #l'action du form se trouve dans cette constante.
    actionFormAddBouteille = '/cave/addBouteille/'


    #c = RefBouteille.objects.all()
    #nbRefBouteille = RefBouteille.objects.count()
    #derniereBouteille = 5
    #listeDerniereBouteille = RefBouteille.objects.all()[nbRefBouteille-derniereBouteille:]
    #listeDerniereBouteille = RefBouteille.objects.all()

    #return render_to_response('html/cave/voirCave.html',{'cave': c, 'bouteilles':b, 'cellules':cellOcc, 'lignes':range(c.lignes), 'colonnes':range(c.colonnes) })


    #return render_to_response('html/cave/stock.html', context_instance=RequestContext(request))
    return render(request,'html/cave/stock.html',{'form': form,'actionFormAddBouteille':actionFormAddBouteille }, context_instance=RequestContext(request))

    #return render_to_response('html/cave/stock.html',{'listeDerniereBouteille':listeDerniereBouteille,'nb':3}, context_instance=RequestContext(request))
    #return render_to_response('html/cave/base.html',"", context_instance=RequestContext(request))

"""
def searchStock(request):
    # recuperation de la liste des bouteille
    post = request.REQUEST['criteria']
    # le post est au format json. On le désérialize

    listeBouteille = RefBouteille.objects.filter( Q(nomB__icontains=post) )
    nbBouteille = listeBouteille.count()

    paginator = Paginator(listeBouteille, 3) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        listeBouteille = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listeBouteille = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listeBouteille = paginator.page(paginator.num_pages)



    return render_to_response('html/cave/stock.html',{'criteria':post,'listeBouteille':listeBouteille,'nbBouteille':nbBouteille}, context_instance=RequestContext(request))
    #return render_to_response('html/cave/stock.html',{'listeDerniereBouteille':listeDerniereBouteille,'nb':3}, context_instance=RequestContext(request))
    #return render_to_response('html/cave/base.html',"", context_instance=RequestContext(request))
"""
"""@csrf_exempt
def searchStockAjaxPost(request):
    # recuperation de la liste des bouteille
    post = request.POST['champs']
    # le post est au format json. On le désérialize
    post = json.loads(post)
    listeBouteille = RefBouteille.objects.filter( Q(nomB__icontains=post) )
    nbBouteille = listeBouteille.count()
    paginator = Paginator(listeBouteille, 4) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        listeBouteille = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listeBouteille = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listeBouteille = paginator.page(paginator.num_pages)


    return HttpResponse(listeBouteille, mimetype="application/json")
"""

@login_required
def searchBouteillesBaseAjax(request):
    if request.is_ajax():
        criteria = request.GET.get('criteriaBouteilleEnBase')
        user = request.user

        if criteria is None:
            criteria =""
        #if criteria is not None:
        if True:
            #listeBouteille = Bouteille.objects.filter( Q(refB__nomB__icontains=criteria),user=user )
            listeBouteille = Bouteille.objects.filter( Q(refB__nomB__icontains=criteria) ,user=user )
            # On liste dans notre stock, les bouteilles qui n'ont pas été bues ni offertes
            listeBouteille = Bouteille.objects.filter( Q(refB__nomB__icontains=criteria) ,user=user, bu=False, offert=False)


            #les ref bouteilles
            #listeBouteille = RefBouteille.objects.filter(maReference__user=user).annotate(num=Count('maReference'))
            #listeBouteille = Bouteille.objects.all()

            nbBouteille = listeBouteille.count()
            paginator = Paginator(listeBouteille, 10) # Show 3 contacts per page
            page = request.GET.get('pageBouteilleEnBase')
            try:
                listeBouteille = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                listeBouteille = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                listeBouteille = paginator.page(paginator.num_pages)

            template = 'html/cave/mesBouteillesEnBaseResultat.html'
            data = {
                'criteriaBouteilleEnBase':criteria,
                'listeBouteille':listeBouteille,
                'nbBouteille':nbBouteille,
            }
            return render_to_response(template, data,
                context_instance = RequestContext(request))
    else:
            raise Http404
@login_required
def searchBouteillesCaveAjax(request):
    if request.is_ajax():
        criteria = request.GET.get('criteriaBouteilleEnCave')
        caveId = request.GET.get('caveId')
        user = request.user

        if criteria is None:
            criteria =""
        #if criteria is not None:
        if True:
            #listeBouteille = Bouteille.objects.filter( Q(refB__nomB__icontains=criteria),user=user )
            listeBouteille = Bouteille.objects.filter( Q(celluleB__cave=caveId) & Q(refB__nomB__icontains=criteria) ,user=user )


            #les ref bouteilles
            #listeBouteille = RefBouteille.objects.filter(maReference__user=user).annotate(num=Count('maReference'))
            #listeBouteille = Bouteille.objects.all()

            nbBouteille = listeBouteille.count()
            paginator = Paginator(listeBouteille, 10) # Show 3 contacts per page
            page = request.GET.get('pageBouteilleEnCave')
            try:
                listeBouteille = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                listeBouteille = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                listeBouteille = paginator.page(paginator.num_pages)

            template = 'html/cave/mesBouteillesEnCaveResultat.html'
            data = {
                'criteriaBouteilleEnCave':criteria,
                'listeBouteille':listeBouteille,
                'nbBouteille':nbBouteille,
                'caveId':caveId,
            }
            return render_to_response(template, data,
                context_instance = RequestContext(request))
    else:
            raise Http404

#@login_required
def searchStockAjax(request):
    #if request.is_ajax():
    if True:

        criteria = request.GET.get('criteria')

        if criteria is None:
            criteria =""
        #if criteria is not None:
        if True:

            # debut de filtrage sur annee, verifier icontains
            listeBouteille = RefBouteille.objects.filter( Q(nomB__icontains=criteria) | Q(anneeB__nom__icontains=criteria) )
            nbBouteille = listeBouteille.count()
            paginator = Paginator(listeBouteille, 2) # Show 3 contacts per page
            page = request.GET.get('page')
            try:
                listeBouteille = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                listeBouteille = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                listeBouteille = paginator.page(paginator.num_pages)

            template = 'html/cave/stockBase.html'
            data = {
                'criteria':criteria,
                'listeBouteille':listeBouteille,
                'nbBouteille':nbBouteille,
            }
            return render_to_response(template, data,
                context_instance = RequestContext(request))
    else:
            raise Http404



@csrf_exempt
def libere_bouteille(request):
    # recuperation de la liste des bouteille
    post = request.POST['list_bouteille']
    # le post est au format json. On le désérialize
    list_bouteille = json.loads(post)
    # on affiche chaque élément. Ici vous devez faire votre traitement, une insertion
    # en base de données par exemple
    for bouteille in list_bouteille:
        nom = bouteille['nom']
        id = bouteille['id']
        id_cave = bouteille['id_cave']
        #x = bouteille['x']
        #y = bouteille['y']
        print ("Placement de "+id+"("+nom+") dans la cave:"+id_cave+" dans le stock")

    #On recupere la bouteille en base
    b=Bouteille.objects.get(id=id)
    #ON recupere la cellule en base
    #cell=Cellule.objects.get(cave=Cave.objects.get(id=id_cave),x=x,y=y)
    #On place la bouteille
    #b.place(cell)
    b.libere()

    # on fait un retour au client
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    # json data est maintenant au format JSON et pret à etre envoyé au client
    return HttpResponse(json_data, mimetype="application/json")


@csrf_exempt
def place_bouteille(request):
    # recuperation de la liste des bouteille
    post = request.POST['list_bouteille']
    # le post est au format json. On le désérialize
    list_bouteille = json.loads(post)
    # on affiche chaque élément. Ici vous devez faire votre traitement, une insertion
    # en base de données par exemple
    for bouteille in list_bouteille:
        #nom = bouteille['nom']
        id = bouteille['id']
        id_cave = bouteille['id_cave']
        x = bouteille['x']
        y = bouteille['y']
        print ("Placement de "+id+" dans la cave:"+id_cave+" sur ligne:"+x+"colonne:"+y)

    #On recupere la bouteille en base
    b=Bouteille.objects.get(id=id)
    #ON recupere la cellule en base
    cell=Cellule.objects.get(cave=Cave.objects.get(id=id_cave),x=x,y=y)
    #On place la bouteille
    b.place(cell)

    # on fait un retour au client
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    # json data est maintenant au format JSON et pret à etre envoyé au client
    return HttpResponse(json_data, mimetype="application/json")

@csrf_exempt
def add_bouteille(request):
    # recuperation de la liste des bouteille
    post = request.POST['list_bouteille']
    # le post est au format json. On le désérialize
    list_bouteille = json.loads(post)
    # on affiche chaque élément. Ici vous devez faire votre traitement, une insertion
    # en base de données par exemple
    for bouteille in list_bouteille:
        nom = bouteille['nom']
        quantite = bouteille['quantite']
        print ("Une bouteille du nom de "+nom+ " et de quantité "+str(quantite))
    # on fait un retour au client
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    # json data est maintenant au format JSON et pret à etre envoyé au client
    return HttpResponse(json_data, mimetype="application/json")

def voirCave(request,cave):
    user = request.user
    # verifier que la cave appartient à l'utilisateur
    c = get_object_or_404(Cave, pk=cave, user=user)

    #Faire le filtrage des bouteilles placées dans cette cave
    #On en filtre pas par el user, la cave appartient deja a l'utilisateur
    b=Bouteille.objects.filter( Q(celluleB__cave_id=1))

    # a modifier
    cellOcc=[b for b in c.mesCellules.select_related() if b.occupe is True]

    return render_to_response('html/cave/voirCave.html',{'cave': c, 'bouteilles':b, 'cellules':cellOcc, 'lignes':range(c.lignes), 'colonnes':range(c.colonnes) })


def populate(request):
    #Par defaut les caves appartiennent au root
    user = User.objects.get(id=1)
   #return render_to_response('home.html', {"foo": "bar"})

    #Annee
    [Annee.objects.get_or_create(nom=str(b),defaults={'nom':str(b),'annee':str(b)+'-01-01'}) for b in range(1800,2050,1)]

    #Cave
    m,n = Cave.objects.get_or_create(user=user, nom="CocoVino",defaults={'nom':'CocoVino'})
   
    #Couleur
    m,n = Couleur.objects.get_or_create(nom="Rosé",defaults={'nom':'Rosé'})
    m,n = Couleur.objects.get_or_create(nom="Rouge",defaults={'nom':'Rouge'})
    m,n = Couleur.objects.get_or_create(nom="Blanc",defaults={'nom':'Blanc'})

    #TypeBouteille
    m,n = TypeBouteille.objects.get_or_create(nom="Magnum",defaults={'nom':'Magnum','volume':'1,5L','ml':1500})
    m,n = TypeBouteille.objects.get_or_create(nom="Double Magnum",defaults={'nom':'Double Magnum','volume':'3L','ml':3000})
    m,n =TypeBouteille.objects.get_or_create(nom="75cl",defaults={'nom':'75cl','volume':'75cl','ml':750})

    #Classification
    m,n = Classification.objects.get_or_create(nom="Grand Cru",defaults={'nom':'Grand Cru'})
    m,n = Classification.objects.get_or_create(nom="Cru Artisan",defaults={'nom':'Cru Artisan'})
    
    #Pays
    m,n = Pays.objects.get_or_create(nom="Argentine",defaults={'nom':'Argentine'})
    m,n = Pays.objects.get_or_create(nom="France",defaults={'nom':'France'})
    
    #Region
    o,p = Region.objects.get_or_create(paysR=m,nom="Alsace",defaults={'paysR':m,'nom':'Alsace'})
    o,p = Region.objects.get_or_create(paysR=m,nom="Bordeaux",defaults={'paysR':m,'nom':'Bordeaux'})
    
    #Cellule
    c = Cave.objects.get(nom="CocoVino")
    A =[(x, y) for x in [xx for xx in range(0,c.colonnes,1)] for y in [yy for yy in range (0,c.lignes,1)] ]
    [ Cellule.objects.get_or_create(cave=c,x=A[X][0],y=A[X][1], defaults={'cave':c,'x':A[X][0],'y':A[X][1]})  for X in range (0,len(A),1)]


    #RefBouteille
    ref,ref2 = RefBouteille.objects.get_or_create(nomB="BouteilleRouge 1",defaults={'nomB':'BouteilleRouge 1','couleurB':Couleur.objects.get(nom='Rouge'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2009')
                                                                     })
    ref,ref2 = RefBouteille.objects.get_or_create(nomB="BouteilleRose 1",defaults={'nomB':'BouteilleRose 1','couleurB':Couleur.objects.get(nom='Rosé'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2005')
                                                                     })
    ref,ref2 = RefBouteille.objects.get_or_create(nomB="BouteilleRouge 2 1",defaults={'nomB':'BouteilleRouge 2','couleurB':Couleur.objects.get(nom='Rouge'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2005')
                                                                     })

    ref,ref2 = RefBouteille.objects.get_or_create(nomB="BouteilleRose 2",defaults={'nomB':'BouteilleRose 2','couleurB':Couleur.objects.get(nom='Rosé'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2005')
                                                                     })

    ref,ref2 = RefBouteille.objects.get_or_create(nomB="BouteilleBlanc 1",defaults={'nomB':'BouteilleBlanc 1','couleurB':Couleur.objects.get(nom='Rosé'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2005')
                                                                     })

    #Bouteille

    """  m,n = Bouteille.objects.get_or_create(nomB="Bouteille 1",defaults={'nomB':'Bouteille 1','couleurB':Couleur.objects.get(nom='Rosé'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      'gardeMinB':Annee.objects.get(nom='2012'),\
                                                                      'gardeMaxB':Annee.objects.get(nom='2020'),\
                                                                      'prixB':'17',\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2009')
                                                                     })
    o,p = Bouteille.objects.get_or_create(nomB="Bouteille 2",defaults={'nomB':'Bouteille 2','couleurB':Couleur.objects.get(nom='Rouge'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      'gardeMinB':Annee.objects.get(nom='2010'),\
                                                                      'gardeMaxB':Annee.objects.get(nom='2015'),\
                                                                      'prixB':'12',\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=1),\
                                                                      'anneeB':Annee.objects.get(nom='2008')

                                                                  })

    """
    # On met a jour les emplacements
    """emp = Cellule.objects.get(cave=c,x=0,y=0)
    emp2 = Cellule.objects.get(cave=c,x=1,y=1)
    m.place(emp)
    o.place(emp2)
    m.libere()
    """

    bigcave,n = Cave.objects.get_or_create(user=user,nom="Bigcave",defaults={'nom':'Bigcave',\
                                           'lignes':10,\
                                           'colonnes':10})
                                           

    return HttpResponse("populate")



