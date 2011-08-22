from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.http import HttpResponse

from greensmoothies.models import DrinkRecord
from greensmoothies.forms import DrinkRecordForm

@csrf_exempt
def drinkrecordcreate(request):
    to_return = ''
    if request.method == 'POST': # If the form has been submitted...
        form = DrinkRecordForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            to_return = 'Success'
    return HttpResponse(to_return)
