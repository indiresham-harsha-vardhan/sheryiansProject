from django import forms
from .models import re,sign

class reform(forms.ModelForm):
    class Meta:
        model=re
        fields='__all__'

class signform(forms.ModelForm):
    class Meta:
        model=sign
        fields='__all__'