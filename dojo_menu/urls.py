from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('programa.views',
    url(r'^$', 'index'),
    url(r'^adicionar/$', 'adicionar'),
    url(r'^salvar/$', 'salvar'),
    url(r'^editar/(?P<pk>\d+)/$', 'editar'),

    #url(r'^admin/', include(admin.site.urls)),
)
