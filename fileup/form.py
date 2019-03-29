from django import forms
from fileup.models import Inputfile


class InputfileForm(forms.ModelForm):
    class Meta:
        model=Inputfile
        fields="__all__"

