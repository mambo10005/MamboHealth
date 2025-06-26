from django import forms 
from .models import HealthRecord
from .utils import get_field_labels

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        exclude = ['user', 'date_recorded']
        widgets = {
            'date_measured': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = get_field_labels()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
