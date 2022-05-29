from django import forms
from django.contrib import admin

class CreateNewsForm(forms.Form):
    news_title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=6000)

class NewsFileForm(forms.Form):
    image_upload = forms.FileField()

class AddNewsFeedForm(forms.Form):
    feed_name = forms.CharField(max_length=60)
    feed_url = forms.CharField(max_length=300)
