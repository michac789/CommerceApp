from django import forms
from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe

from .models import User


class SSOForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
    
    def __init__(self, *args, **kwargs):
        super(SSOForm, self).__init__(self, *args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'something'
        })
