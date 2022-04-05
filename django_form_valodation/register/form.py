from django.core.exceptions import ValidationError
from django import forms
import re


def mail_validator(value):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, value):
        raise ValidationError('Not a valid email')
    return value

def pass_validator(value):
    if len(value)<6:
        raise ValidationError('very very short')
    return value

class RegisterForm(forms.Form):
    f_name = forms.CharField(max_length=50,label='First Name',widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    l_name = forms.CharField(max_length=50,label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Enter your Last name'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),validators=[pass_validator])
    pasword = forms.CharField(max_length=50,label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),validators=[pass_validator])
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
    
    def clean_f_name(self):
        data = self.cleaned_data['f_name']
        if len(data)<5 or len(data)>10:
            raise ValidationError('Not a real name')
        return data
    
    def clean_l_name(self):
        data = self.cleaned_data['l_name']
        if len(data)<5 or len(data)>10:
            raise ValidationError('Not a real name')
        return data
    def clean_email(self):
        data = self.cleaned_data['email']
        return mail_validator(data)
    def clean_pasword(self):
        data = self.cleaned_data['pasword']
        return pass_validator(data)

    

        


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}))
    pasword = forms.CharField(max_length=50,label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}))
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
    def clean_email(self):
        data = self.cleaned_data['email']
        return mail_validator(data)
    def clean_pasword(self):
        data = self.cleaned_data['pasword']
        return pass_validator(data)  
