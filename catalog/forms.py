from django import forms 
from catalog.models import Car

gearbox_mech = 1
gearbox_auto = 2
gearbox_robot = 3
gearbox_null = 4

GEARBOX_CHOICES = [
    (gearbox_mech, "Механика"),
    (gearbox_auto, "Автомат"),
    (gearbox_robot, "Робот"),
    (gearbox_null, "Любое"),
]

class SearchForm(forms.Form):  
    #manufacturer = forms.CharField(max_length=128, required=False)
    model = forms.CharField(max_length=56, required=False, label='Поиск')
    #year = forms.IntegerField(required=False)
    gearbox = forms.IntegerField(widget=forms.Select(choices=GEARBOX_CHOICES), required=False)
    #color = forms.CharField(max_length=128, required=False)