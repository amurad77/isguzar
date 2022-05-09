from django import forms
from comments.models import ArticleComments, NewsComments


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComments

        fields = (
            'name',
            'mail',
            'subject',
            'message'
        )

        widgets = {
            'name' : forms.TextInput(attrs = {
                                'class' : 'form-control',
                                'id' : 'email',
                                'placeholder' : 'Enter Name'
                                }),
            'mail' : forms.EmailInput(attrs = {
                                'class' : 'form-control',
                                'id' : 'email',
                                'placeholder' : 'Enter email address',
                                }),
            'subject' : forms.TextInput(attrs = {
                                'class' : 'form-control',
                                'id' : 'email',
                                'placeholder' : 'Subject',
                                }),
            'message' : forms.TextInput(attrs = {
                                'class' : 'form-control mb-10',
                                'id' : 'email',
                                'placeholder' : 'Messege',
                                })
        }



class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComments

        fields = (
            'name',
            'mail',
            'subject',
            'message'
        )

        widgets = {
            'name' : forms.TextInput(attrs = {
                                'class' : 'form-control',
                                'id' : 'email',
                                'placeholder' : 'Enter Name'
                                }),
            'mail' : forms.EmailInput(attrs = {
                                'class' : 'form-control',
                                'id' : 'email',
                                'placeholder' : 'Enter email address',
                                }),
            'subject' : forms.TextInput(attrs = {
                                'class' : 'form-control',
                                'id' : 'email',
                                'placeholder' : 'Subject',
                                }),
            'message' : forms.TextInput(attrs = {
                                'class' : 'form-control mb-10',
                                'id' : 'email',
                                'placeholder' : 'Messege',
                                })
        }