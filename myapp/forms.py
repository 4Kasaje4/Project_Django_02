from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import member , postdata

class RegisterForm(UserCreationForm):
        email = forms.CharField(max_length=100 ,widget=forms.EmailInput(attrs={'class' : 'form-control mt-2 mb-3' , }) )
        first_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class' : 'form-control mt-2 mb-3'}))
        last_name = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class' : 'form-control mt-2 mb-3'}))
        username = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class' : 'form-control mt-2 mb-3'}))
        password1 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class' : 'form-control mt-2 mb-3'}) , label='Password')
        password2 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class' : 'form-control mt-2 mb-3'}) , label='Confirm password')


        class Meta:
            model = User
            fields = ['username', 'email', 'first_name', 'last_name', 'password1' , 'password2']


class UserProfileForm(forms.ModelForm):
        first_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class' : 'form-control mt-2 mb-3'}))
        last_name = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class' : 'form-control mt-2 mb-3'}))
        class Meta:
            model = User
            fields = ('first_name' , 'last_name' ,)


class ExtendedProlfileForm(forms.ModelForm):
      phone = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control mt-2 mb-3'}))
      class Meta:
            model = member
            fields = ( 'phone' ,)



class PostForm(forms.ModelForm):
      description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control mt-2 mb-3 w-100'}) , label="Type your post")
      class Meta:
            model = postdata
            fields = ('description',)

class PasswordChangingForm(PasswordChangeForm):
      old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control mt-2 mb-3 w-100' , 'type' : 'password'}) , label="Old password")
      new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control mt-2 mb-3 w-100', 'type' : 'password'}) , label="New password")
      new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control mt-2 mb-3 w-100' ,'type' : 'password'}) , label="Comfirm password")

      class Meta:
            model = User
            fields = ('old_password' , 'new_password1' , 'new_password2')