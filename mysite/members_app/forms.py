from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        label="Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class': "form-control"})
    )
    last_name = forms.CharField(
        max_length=100,
        label="Surname",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': "form-control"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'class': "form-control"})
    )
    phone = forms.CharField(
        max_length=20,
        label="Phone number",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': "form-control"})
    )
    address = forms.CharField(
        max_length=255,
        label="Address",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': "form-control"}),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'class': "form-control"}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': "form-control"}),
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': "form-control"}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': "form-control"}),
        label="Password"
    )