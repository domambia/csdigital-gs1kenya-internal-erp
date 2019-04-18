from django import forms 
from CRM.models import Client, Training, Note

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
        fields = ('trainer', 'happened_on','all_trainee', 'description')

class EditClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('member_number', 'member_prefix')

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields  = ('notes',)
