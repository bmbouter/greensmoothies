from django.forms import ModelForm
from greensmoothies.models import DrinkRecord

from greensmoothies import fields as greensmoothies_fields

class DrinkRecordForm(ModelForm):
    recaptcha = greensmoothies_fields.ReCaptchaField()

    class Meta:
        model = DrinkRecord
