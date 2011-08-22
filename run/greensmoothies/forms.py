from django.forms import ModelForm
from greensmoothies.models import DrinkRecord

class DrinkRecordForm(ModelForm):
    class Meta:
        model = DrinkRecord
