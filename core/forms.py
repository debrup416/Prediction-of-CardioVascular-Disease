from django.forms import ModelForm, fields
from .models import cardioVascular

class cardioVascularForm(ModelForm):
    class Meta:
        model=cardioVascular
        fields= '__all__'

