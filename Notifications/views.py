from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from Notifications.forms import PushNotificationForm
from services.models.Notifications import PushNotification
from utilities.fcm_manager import sendPush

class PushNotifications(LoginRequiredMixin, TemplateView):
    template_name = "notifications/push-notifications.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        form = PushNotificationForm(request.POST or None)
        if form.is_valid():
            notification = PushNotification(
                form.cleaned_data['notification_title'],
                form.cleaned_data['notification_image_url'],
                form.cleaned_data['notification_body']
            )
            print(notification)
            # Enter Registration Token
            sendPush(notification["notification_title"], notification["notification_body"], ["749ddedeueiej7978733e33df5gvt"])
        return HttpResponseRedirect(reverse('notifications'))
