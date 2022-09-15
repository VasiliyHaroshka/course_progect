from django import forms
from .models import *


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Выберите группу товара'

    class Meta:
        model = Balloon
        fields = ['name',
                  'slug',
                  'description',
                  'price', 'photo',
                  'is_onsite',
                  'group']
        widgets = {'description': forms.Textarea(attrs={'cols': 60, 'rows': 15})}
