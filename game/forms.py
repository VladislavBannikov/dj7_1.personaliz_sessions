from django import forms
# from django.core.validators import MaxValueValidator, MinValueValidator

class InputForm(forms.Form):
    number = forms.IntegerField(label="Число")
