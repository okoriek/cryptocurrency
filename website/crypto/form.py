from django import forms
from django.forms import fields
from .models import Membership, Price, UserMembership
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CustomForm(forms.ModelForm):
    class Meta:
        model=UserMembership
        exclude = '__all__'

class RegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password1','password2')


class SubcriptionForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('price', 'subcription')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].queryset = Price.objects.none()

        if 'subcription' in self.data:
            try:
                subcription_id = int(self.data.get('subcription'))
                self.fields['price'].queryset = Price.objects.filter(subcription_id=subcription_id).order_by('price')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['price'].queryset = self.instance.subcription.price_set.order_by('price')
      

            
        
        
    