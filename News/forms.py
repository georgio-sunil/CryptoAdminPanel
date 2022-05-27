from django import forms
from django.contrib import admin

class CreateNewsForm(forms.Form):
    OPTIONS = (
        ("ETH", "Ethereum"),
        ("ADA", "Cardano"),
    )
    news_title = forms.CharField(max_length=30)
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)
    content = forms.CharField(max_length=300)

class NewsFileForm(forms.Form):
    image_upload = forms.FileField()

class AddNewsFeedForm(forms.Form):
    feed_name = forms.CharField(max_length=60)
    feed_url = forms.CharField(max_length=300)
