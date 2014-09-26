from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
    url(r'^todos/$', 'store.views.articulos'),
    url(r'^obtener/(lt;articulo_id>\d+)/$', 'store.views.articulo'),
)
