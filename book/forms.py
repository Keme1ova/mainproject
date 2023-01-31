from django import forms
from . import models


class Form_notes(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'