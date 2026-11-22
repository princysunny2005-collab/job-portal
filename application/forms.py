from django import forms
from . models import RegisterModel

class RegisterModelForms(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields = "__all__" 
class UpdateForm(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields ="__all__"

# class RegisterViewForm(forms.ModelForm):
#     class Meta:
#         model =RegiterViewModel
#         fields ="__all__"
