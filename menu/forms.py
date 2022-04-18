from django import forms

class MenuForm(forms.Form):
    id = forms.IntegerField(label='ID')
    