from django import forms
from .models import Menu
from . import models

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'calorie', 'protein', 'fat', 'carbohydrates', 'dietary_fiber', 'favorite']


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))


        