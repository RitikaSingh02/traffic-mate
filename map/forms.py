from django import forms

class NameForm(forms.Form):
    Pickup = forms.CharField(label='Pickup Location' , required=True)
    Drop = forms.CharField(label='Drop Location' , required=True)