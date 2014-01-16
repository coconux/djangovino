from django.conf.urls import patterns, url

from cave import views



urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^populate/', views.populate, name='populate'),
    url(r'^testcave/', views.testcave, name='testcave'),
    url(r'^home/', views.home, name='home'),
    url(r'^stock/', views.stock, name='stock'),
    #url(r'^searchStock$', views.searchStock, name='searchStock'),
    url(r'^searchStockAjax$', views.searchStockAjax, name='searchStockAjax'),
    url(r'^searchBouteillesAjax$', views.searchBouteillesAjax, name='searchBouteillesAjax'),
    url(r'^voirCave/(?P<cave>\d+)/$', views.voirCave, name='voirCave'),
    url(r'^mesCaves/', views.mescaves, name='mescaves'),
    url(r'^gererCave/(?P<num>\d+)/$', views.gerercave, name='gerercave'),
    #url(r'^addToStockFromRef/(?P<idRef>\d+)/$', views.addToStockFromRef, name='addToStockFromRef'),
    url(r'^addToStockFromRef$', views.addToStockFromRef, name='addToStockFromRef'),

    url(r'^RefBouteilleList/$', views.RefBouteilleList.as_view()),
    url(r'^list/([\w-]+)/$', views.TousLesUtilisateurs.as_view()),


    url(r'^add_bouteille$', views.add_bouteille, name='add_bouteille'),
    url(r'^place_bouteille$', views.place_bouteille, name='place_bouteille'),
    url(r'^libere_bouteille$', views.libere_bouteille, name='libere_bouteille'),


    #url(r'^$', views.TicketView, name='TicketView')
)
