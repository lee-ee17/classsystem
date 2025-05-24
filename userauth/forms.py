from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class register_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class': 'form-control'
        }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder':'Comfirm Password',
    'class': 'form-control'
    }))
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={
                'placeholder':'Username',
                'class': 'form-control'
                }),
            'email':forms.EmailInput(attrs={
                'placeholder':'Email',
                'class': 'form-control'
                }),
        }
           
def clean_username(self):
    username=self.cleaned_data.get('username')
    if User.objects.filter(username=username).exists():
        raise ValidationError("使用者名稱已被使用")
    return username
def clean_confirm_password(self):
    password=self.cleaned_data.get('password')
    confirm=self.cleaned_data.get('confirm')
    if password and confirm and password!=confirm:
        raise ValidationError("密碼不相同")
    return confirm
class login_form(forms.Form):
    username=forms.CharField(
        label='Username',
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder':'Username',
            'class':'form-control'
        })
    )
    password=forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder':'Password',
            'class': 'form-control'
        })
    )