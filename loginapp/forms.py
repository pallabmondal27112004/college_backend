from django import forms
from .models import customeruser
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    class Meta:

        model = customeruser  
        fields = ['first_name', 'last_name','email','catagory','phone', 'image','password']  # List of fields to include in the form
        labels={
            'first_name':"", 'last_name':"",'email':"",'password':"",'phone':""

        }
        widgets = {
            'email': forms.EmailInput(attrs={'id':'inputset',' class': ' me-3 w-100 md-form-control', 'placeholder': 'Email' }),
            'first_name': forms.TextInput(attrs={'id':'inputset',' class': ' me-3 md-form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'id':'inputset',' class': ' me-3 md-form-control', 'placeholder': 'Last name'}),
            # 'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.TextInput(attrs={'id':'inputset',' class': ' me-3  md-form-control', 'placeholder': 'Password'}),
            'phone': forms.TextInput(attrs={'id':'inputset',' class': ' me-3 md-form-control', 'placeholder': 'Phone no.'}),
            # 'catagory': forms.RadioSelect(attrs={'class': 'ps-2 fs-6 ',}),
        }
  