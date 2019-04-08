from django import forms
from ACCNTS.models import Invoice
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('amount',)

class SearchForm(forms.ModelForm):
    start = forms.DateTimeField()
    end = forms.DateTimeField()
