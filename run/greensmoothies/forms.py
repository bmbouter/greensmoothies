from django.forms import ModelForm
from greensmoothies.models import DrinkRecord

from greensmoothies import fields as greensmoothies_fields

class DrinkRecordForm(ModelForm):
    recaptcha = greensmoothies_fields.ReCaptchaField()

    class Meta:
        model = DrinkRecord
        #exclude = ('lat', 'lng')

    #def __init__(self, *args, **kwargs):
    #    super(DrinkRecordForm, self).__init__(*args, **kwargs)
    #    if kwargs.has_key('instance'):
    #        instance = kwargs['instance']
    #        self.initial['recaptcha'] = instance.recaptcha

    #def save(self, commit=True):
    #    model = super(DrinkRecordForm, self).save(commit=False)
    #    model.recaptcha = self.cleaned_data['recaptcha']
    #    if commit:
    #        model.save()
    #    return model
