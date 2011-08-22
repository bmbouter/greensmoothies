from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.auth.decorators import login_required

from greensmoothies.views import HomepageView

urlpatterns = patterns('greensmoothies.views',
    url(r'^$', HomepageView.as_view(), name='homepage_url'),
    url(r'^drinkrecord/$', 'drinkrecordcreate', name='drink_record_create_url'),
)
