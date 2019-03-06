from django import forms
from hrm.models import Performance 

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ('notes',)
