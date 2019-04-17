from django import forms
from ACCNTS.models import Invoice,PayRoll
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('amount',)

class SearchForm(forms.ModelForm):
    start = forms.DateTimeField()
    end = forms.DateTimeField()

class PayRollForm(forms.ModelForm):
	class Meta:
		model = PayRoll
		fields = (
				'employee', 
				'pension', 
				'lunch', 
				'month'
			)