from django import forms

from .models import Item, Seller


class ItemForm(forms.ModelForm):
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
        

class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['location']
