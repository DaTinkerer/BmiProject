from django import forms

class English_UnitsForm (forms.Form):
    weight_lbs = forms.FloatField(min_value=0,
    widget=forms.NumberInput(attrs={'placeholder': 'lbs'}))

    height_ft = forms.IntegerField(min_value=0,
    widget=forms.NumberInput({'placeholder': 'ft'}))
    height_in = forms.IntegerField(min_value=0,
    widget=forms.NumberInput(attrs={'placeholder': 'in'}))
    
class Metic_UnitsForm (forms.Form):
    weight_kg = forms.IntegerField(min_value=0,
    widget=forms.NumberInput(attrs={'placeholder': 'Kg'}))
    height_cm = forms.IntegerField(min_value=0,
    widget=forms.NumberInput(attrs={'placeholder': 'cm'}))
    