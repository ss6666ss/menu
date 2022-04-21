from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields   = ['name', 'calorie', 'protein', 'fat', 'carbohydrates', 'dietary_fiber']
        