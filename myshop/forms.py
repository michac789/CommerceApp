from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe

from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'price', 'category']
    
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget = forms.TextInput(attrs={
            "class": "abc"
        })
