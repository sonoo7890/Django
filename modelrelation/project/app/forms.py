from django import forms
from .models import Student, Aadhar


class AadharForm(forms.ModelForm):
    class Meta:
        model = Aadhar
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_adhar_no(self):
        adhar = self.cleaned_data.get('adhar_no')
        if Student.objects.filter(adhar_no=adhar).exists():
            raise forms.ValidationError("This Aadhaar number already exists.")
        return adhar