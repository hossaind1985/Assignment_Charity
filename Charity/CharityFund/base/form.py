from django import forms
from base.models import charity

class charities(forms.ModelForm):

    class Meta:
        model = charity
        fields = '__all__'