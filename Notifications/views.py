from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.base import TemplateView
from rest_framework.response import Response
from Notifications.forms import PushNotificationForm
from rest_framework.decorators import api_view
from services.models.Notifications import PushNotification
from utilities.fcm_manager import getNotificationsFromFCM, sendPush
from utilities.uploadFile import saveFile


class PushNotifications(LoginRequiredMixin, TemplateView):
    template_name = "notifications/push-notifications.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        form = PushNotificationForm(request.POST or None)
        if form.is_valid():
            image_url = saveFile(request.FILES['image_upload'], 'notification_images')
            notification = PushNotification(
                form.cleaned_data['notification_title'],
                image_url,
                form.cleaned_data['notification_body']
            )
            # Enter Registration Token
            check = sendPush(notification["notification_title"], notification["notification_body"], notification["notification_image_url"], ["fnclq8tQZ0cLrVjxokDvZh:APA91bGhcEBsJxOfMHLGIGs6y4WsdvEqsCy3_vrmuh2qCRXL4ae2ipmCqwUnGwdoJgn-WXz9eVlC1bpZrZpgom-dfNUMlPD7edLG_-UyMZgrSlZHNQVXlYuqae9-LBn7kcN-nKYOC8Fh",
            "fs0Td-mwSRegB8UccRG076:APA91bEZFYsdJ6WcjOz55R_fXv_OGNW1mwQR9txTLRDLephNpZUj3xE9zNP_PbcHMizzTSsFODVe3pxWuC_3ErEGf5jqdUXce4npfdJTmhlhN31Ei2yVrS9dVCUKOFl9-x6Vf9QjBMZf"])
            if check:
                messages.success(self.request, 'Notification sent successfully')
            else:
                messages.error(self.request, "Notification not sent")
            return HttpResponseRedirect(self.request.path_info)
        return HttpResponseRedirect(reverse('notifications'))

# API for fetching Notifications from Firestore.
@api_view(['GET'])
def getNotifications(request):
    notifications = getNotificationsFromFCM()
    print(notifications)
    if request.method == 'GET':
        return Response(notifications)
    return Response({"message" : "Nice try.."})