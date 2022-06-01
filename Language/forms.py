from django import forms
from django.contrib import admin

class AddLanguageForm(forms.Form):
    locale_name = forms.CharField(max_length=100)
    language_name = forms.CharField(max_length=100)

class UpdateLanguageForm(forms.Form):
    locale_name = forms.CharField(max_length=100)
    language_name = forms.CharField(max_length=100)