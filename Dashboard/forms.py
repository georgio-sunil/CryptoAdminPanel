from django import forms
from django.contrib import admin

class LoginModelForm(forms.Form):
    username = forms.CharField(max_length=30)
    userpassword = forms.CharField(max_length=30)