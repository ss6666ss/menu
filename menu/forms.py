from django import forms

class MenuForm(forms.Form):
    id = forms.IntegerFielld(label='ID')
    name = forms.CharField(label='name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    calorie = forms.IntegerField(label='calorie', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    protein = forms.IntegerField(label='protein', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    fat = forms.IntegerField(label='fat', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    carbohydrates = forms.IntegerField(label='carbohydrates', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    dietary_fiber = forms.IntegerField(label='dietary_fiber', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))


