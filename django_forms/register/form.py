from typing import Type
from django import forms
class RegisterForm(forms.Form):
    f_name = forms.CharField(max_length=50,label='First Name',widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    l_name = forms.CharField(max_length=50,label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Enter your Last name'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}))
    pasword = forms.CharField(max_length=50,label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}))
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}))
    pasword = forms.CharField(max_length=50,label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}))
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)   
