from django import forms
from .models import food


class FoodForm(forms.ModelForm):
    class Meta:
        model = food
        fields = ('name', 'body')
