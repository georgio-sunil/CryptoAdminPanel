from django import forms

class PushNotificationForm(forms.Form):
    notification_title = forms.CharField(max_length=50)
    # notification_image_url = forms.CharField(max_length=50)
    notification_body = forms.CharField(max_length=150)