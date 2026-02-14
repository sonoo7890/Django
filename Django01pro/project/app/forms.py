# from django import forms

# class RegForm(forms.Form):
#     Name=forms.CharField()
#     Email=forms.EmailField()
#     contact=forms.IntegerField()

from django import forms
from .models import Registration

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
