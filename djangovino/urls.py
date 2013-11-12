from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from registration.views import RegistrationView
#from registration.forms import RegistrationFormTermsOfService
 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wickets.views.home', name='home'),
    # url(r'^wickets/', include('wickets.foo.urls')),
    #url(r'^home/', include('ticket.urls')),
    url(r'^cave/', include('cave.urls')),
    #url(r'^auth/', include('login.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #(r'^account/', include('registration.backends.default.urls')),





)


