from django import forms 
from leave.models import ApplyLeave

class ApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyLeave
        fields = (
            'start_date', 'resume_date', 'home_phone','person_taking_charge', 'leave', 'employee',
            'end_date'
        )
    def __str__(self):
        return self.employee
    