from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')
        
        labels = {
            'username'      : '',
            'first_name'    : '',
            'last_name'     : '',
            'email'         : '',
            
            # password modification fields didnt work here
            # 'password1'     : '',
            # 'password2'     : '',
        }
        widgets = {
            'username'      : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email'         : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            
            # password fields modification didnt work here
            
            # 'password1'     : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            # 'password2'     : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        }
           
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Must contains uppercase, lowercase, numbers and special characters not less than 8 </span>'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Repeat password here</span>'
        