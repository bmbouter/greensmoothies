from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.auth.decorators import login_required

from greensmoothies.views import PageView

urlpatterns = patterns('greensmoothies.views',
    url(r'^$', PageView.as_view(template_name="greensmoothies/home.html"), name='homepage_url'),
    url(r'^about/$', PageView.as_view(template_name="greensmoothies/about.html"), name='about_url'),
    url(r'^drinkrecord/$', 'drinkrecordcreate', name='drink_record_create_url'),
)
