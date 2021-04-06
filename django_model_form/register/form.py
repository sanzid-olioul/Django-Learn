from django import forms
from .models import UserRegister,UserLogin
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
    class Meta:
        model = UserRegister
        fields = '__all__'
        widgets = {
            'f_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'l_name': forms.TextInput(attrs={'placeholder': 'Enter your Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),
        }
        labels = {
            'f_name':'First Name',
            'l_name': 'Last Name',
            'email': 'Email',
            'password':'password',
        }
    


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
    class Meta:
        model = UserLogin
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),
        }
        labels = {
            'email': 'Email',
            'password':'Password',
        }
       
