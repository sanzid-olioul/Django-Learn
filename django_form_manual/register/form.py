from typing import Type
from django import forms
class RegisterForm(forms.Form):
    f_name = forms.CharField(max_length=50,label='First Name',help_text='Enter your first name')
    l_name = forms.CharField(max_length=50,label='Last Name',help_text='Enter your last name')
    email = forms.EmailField(label='Email',help_text='Enter your email')
    pasword = forms.CharField(max_length=50,label='Password',widget=forms.PasswordInput())