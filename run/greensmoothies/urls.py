from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

urlpatterns = patterns('pentairweb.views',
    url(r'^$', TemplateView.as_view(template_name="greensmoothies/homepage.html"), name='homepage_url'),
    url(r'^map.html$', TemplateView.as_view(template_name="greensmoothies/map.html"), name='map_url'),
)


#from django.conf.urls.defaults import patterns, include, url
#urlpatterns = patterns('',
#    # Examples:
#    url(r'^/?$', 'dose_mobile.views.home', name='home'),
#
#    url(
#        r'^accounts/login/$','django.contrib.auth.views.login',
#        dict(
#            template_name = 'jqm/login.html',
#        ),
#        name='login',
#    ),
#    url(
#        r'^accounts/logout/$','django.contrib.auth.views.logout',
#        dict(
#            template_name = 'jqm/logout.html',
#        ),
#        name='logout',
#    ),
#
#)