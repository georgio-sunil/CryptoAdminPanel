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
            sendPush(notification["notification_title"], notification["notification_body"], notification["notification_image_url"], ["fnclq8tQZ0cLrVjxokDvZh:APA91bGhcEBsJxOfMHLGIGs6y4WsdvEqsCy3_vrmuh2qCRXL4ae2ipmCqwUnGwdoJgn-WXz9eVlC1bpZrZpgom-dfNUMlPD7edLG_-UyMZgrSlZHNQVXlYuqae9-LBn7kcN-nKYOC8Fh",
            "fs0Td-mwSRegB8UccRG076:APA91bEZFYsdJ6WcjOz55R_fXv_OGNW1mwQR9txTLRDLephNpZUj3xE9zNP_PbcHMizzTSsFODVe3pxWuC_3ErEGf5jqdUXce4npfdJTmhlhN31Ei2yVrS9dVCUKOFl9-x6Vf9QjBMZf"])
        return HttpResponseRedirect(reverse('notifications'))
