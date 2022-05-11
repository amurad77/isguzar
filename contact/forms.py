from django import forms
from .models import Subscribe, Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'messege',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'Enter your name',
                                    'id': 'value'
                                    
                                }),
            'email': forms.EmailInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'Enter email address',
                                    'id': 'value1'
                                    
                                }),
            'subject': forms.TextInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'Enter subjects',
                                    'id': 'value2'
                                }),
            'messege': forms.Textarea(attrs={
                                    'class': 'common-textarea form-control',
                                    'placeholder': 'Enter Messege',
                                    'id': 'value3'
                                })
        }








class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe

        fields = (
            'email',
        )

        widgets = {

            'email' : forms.EmailInput(attrs = {
                                'class' : 'form-control',
                                'id' : 'value_remove',
                                'placeholder' : 'Enter email address',
                                })
                   
        }

