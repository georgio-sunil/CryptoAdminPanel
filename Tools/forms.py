from django import forms
from django.contrib import admin

class AddBannersForm(forms.Form):
    banner_title = forms.CharField(max_length=100)
    banner_text = forms.CharField(max_length=100)
    banner_color = forms.CharField(max_length=100)
    button_text = forms.CharField(max_length=100)
    button_link = forms.CharField(max_length=100)

class UpdateBannerForms(forms.Form):
    banner_title = forms.CharField(max_length=100)
    banner_text = forms.CharField(max_length=100)
    banner_color = forms.CharField(max_length=100)
    button_text = forms.CharField(max_length=100)
    button_link = forms.CharField(max_length=100)

class FAQForms(forms.Form):
    faq_question = forms.CharField(max_length=100)
    faq_answer = forms.CharField(max_length=1000)