from django import forms
from .models import Menu, Cook
from . import models

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'calorie', 'protein', 'fat', 'carbohydrates', 'dietary_fiber', 'favorite']

class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ['menu', 'title', 'price', 'weight']

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))


        