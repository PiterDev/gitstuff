from django import forms
from .models import Repo

class ChooseRepoForm(forms.Form):
    owner = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Owner'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    # save
    def save(self):
        repo = Repo(owner=self.cleaned_data['owner'], name=self.cleaned_data['name'])
        repo.save()