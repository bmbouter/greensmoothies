from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import TemplateView
from django.contrib.sites.models import Site
from django.http import HttpResponse

from greensmoothies.models import DrinkRecord
from greensmoothies.forms import DrinkRecordForm

@csrf_exempt
def drinkrecordcreate(request):
    to_return = '{ "status": "fail" }'
    if request.method == 'POST': # If the form has been submitted...
        form = DrinkRecordForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            to_return = '{ "status": "success" }'
    return HttpResponse(to_return)

class HomepageView(TemplateView):
    template_name = "greensmoothies/homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        context['recaptcha_field'] = DrinkRecordForm()['recaptcha']
        return context
