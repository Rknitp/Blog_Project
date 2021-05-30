from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
#In place of UserRegisterForm  any name it is just name of a class
class UserRegisterForm(UserCreationForm):#We make a new class and inherit UserCreationForm
    email=forms.EmailField() #EmailField() takes an argument named required which is by default true means (compulsary)

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model=User #model we want to wotk with
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile #model(profile class we have made) we want to wotk with
        fields = ['image']
