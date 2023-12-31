from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
   # email = forms.EmailField(required=True)
   username = forms.CharField(required=True)
   password = forms.CharField(required=True, widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
   email = forms.EmailField(required=True)
   class Meta:
      model = User
      fields = ["username","email", "password1", "password2"]