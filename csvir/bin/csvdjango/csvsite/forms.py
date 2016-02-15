from django import forms
from .models import CsvData

class CsvDataForm(forms.ModelForm):
    class Meta:
        model=CsvData
        field=('adres','durum','hedef_adres','zaman')
        exclude={}
