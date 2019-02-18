from django import forms 
from CRM.models import Client, Training

def get_clients():
    list_clients = Client.objects.all()
    clients = []
    for cl in list_clients:
        clients.append((cl.id, cl.company_name ,))
    return tuple(clients)


class TrainForm(forms.ModelForm):
    all_trainee = forms.MultipleChoiceField(widget=forms.SelectMultiple,
                                             choices=get_clients())
    class Meta:
        model = Training
        fields = ('trainer', 'number_of_trainee', 'happened_on','all_trainee')
