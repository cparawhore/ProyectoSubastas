from django.conf.urls import patterns, include, url
from django.contrib import admin
from store.views import RegistrarUsuario

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#(r'^articulos/', include('store.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'store.views.home', name='home'),
    url(r'^login/', 'store.views.iniciar_sesion', name='login'),
    url(r'^signup/$','store.views.register_view',name='vista_registro'),
    #url(r'^accounts/', include('registration.urls')),
)
