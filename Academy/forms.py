from django import forms
from django.contrib import admin

class AddCourseForm(forms.Form):
    course_name = forms.CharField(max_length=200)
    # course_tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #                                       choices=OPTIONS)
    course_url = forms.CharField(max_length=200)
    course_color = forms.CharField(max_length=30)
    topic_count = forms.IntegerField(max_value=10)
    video_count = forms.IntegerField(max_value=10)
    course_desc = forms.CharField(max_length=500)

class UpdateCourseForm(forms.Form):
    course_name = forms.CharField(max_length=200)
    # course_tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #                                       choices=OPTIONS)
    course_url = forms.CharField(max_length=200)
    course_color = forms.CharField(max_length=30)
    topic_count = forms.IntegerField(max_value=10)
    video_count = forms.IntegerField(max_value=10)
    course_desc = forms.CharField(max_length=500)

class TopicForm(forms.Form):
    topic_name = forms.CharField(max_length=50)
    topic_desc = forms.CharField(max_length=200)
    topic_type = forms.CharField(max_length=50)
    topic_url = forms.CharField(max_length=100)
    
class TopicFileUploadForm(forms.Form):
    topic_url = forms.FileField()
    topic_content = forms.FileField()

class AddCategoryForm(forms.Form):
    category_type = forms.CharField(max_length=50)
    category_name = forms.CharField(max_length=50)
