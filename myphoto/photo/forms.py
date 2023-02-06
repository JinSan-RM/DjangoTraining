from django import forms
from .models import photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = photo
        fields = ('title','author','image',
        'description','price')