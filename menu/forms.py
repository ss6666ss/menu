from django import forms
from .models import Menu

class MenuForm(forms.Form):
    class Meta:
        model = Menu
        menus   = ['name', 'calorie', 'protein', 'fat', 'carbohydrates', 'dietary_fiber']