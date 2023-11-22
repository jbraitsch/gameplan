from django.forms import ModelForm
from .models import Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'is_open','email', 'address', 'city', 'phone_number', 'about')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']