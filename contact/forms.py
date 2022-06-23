from django import forms
from .models import Subscribe, Contact, Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = (
            'name_surname',
            'mail',
            'phono',
            'education_industry',
            'subjects',
        )

        widgets = {
            'name_surname': forms.TextInput(attrs={
                                            'class': 'common-input mb-20 form-control',
                                            'placeholder': 'Ad ve Soyad',
                                            }),
            'mail': forms.TextInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'E-Mail adres',
            
                                    }),
            'phono': forms.TextInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'Telefon',
                                    }),
            'education_industry': forms.TextInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'Təhsil və sənayə təcrübəniz',
                                    }),
            'subjects': forms.TextInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'Hansı mövzuda yaza bilərsiniz?',
                                    }),
        }

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

            'email': forms.EmailInput(attrs={
                                    'class': 'common-input mb-20 form-control',
                                    'placeholder': 'Enter email address',
                                    'id': 'value1'
                                    
                                })
        }
