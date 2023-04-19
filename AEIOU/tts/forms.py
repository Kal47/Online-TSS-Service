from django import forms

class PhraseForm(forms.Form):
    phrase = forms.CharField(label='phrase')
