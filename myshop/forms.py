from django.forms import ModelForm, Textarea
from django import forms
from django.utils.safestring import mark_safe

from .models import Item, Seller


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'price', 'category']
    
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for field in ['title', 'image', 'price', 'description']:
            tmp = self.fields[field].widget
            tmp.attrs["class"] = "form-control"
        self.fields['image'].label = 'Image link'
        self.fields['price'].label = 'Price (in $)'
        self.fields['description'].widget = forms.Textarea(attrs={
            "class": "form-control", "rows": 2, "maxlength": 256,
        })
        self.fields['price'].widget.attrs["min"] = 0
        self.fields['price']
        self.fields['category'].widget.attrs["class"] = "form-select"
        self.fields['category'].empty_label = 'Select a category here'
        

class SellerRegistrationForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['location']
        
    def __init__(self, *args, **kwargs):
        super(SellerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["location"].widget = forms.TextInput(attrs={
            
        })
