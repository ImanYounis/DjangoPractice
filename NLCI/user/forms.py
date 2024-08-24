from django import forms
from .models import Emp
from django.forms import inlineformset_factory
from .models import Master, Detail

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['eName', 'deptID', 'gender']
        widgets = {
            'gender': forms.RadioSelect
        }

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['name']

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['description']  # Ensure this line is included

DetailFormSet = inlineformset_factory(Master, Detail, form=DetailForm, extra=1, can_delete=True)