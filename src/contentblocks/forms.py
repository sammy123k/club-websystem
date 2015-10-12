from django import forms

from .models import Block

class BlockForm(forms.ModelForm):
  class Meta:
    model = Block
    fields = ['datatype', 'published', 'blob']
