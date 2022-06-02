from datetime import datetime
import uuid
import firebase_admin
from firebase_admin import credentials, messaging, firestore

cred = credentials.Certificate("utilities/credentials/wm-notifications-firebase-adminsdk.json")
app = firebase_admin.initialize_app(cred)

def sendPush(title, msg, image, registration_token, dataObject=None):
    # print(app.name, app.project_id)
    # message = messaging.MulticastMessage(
    #     notification=messaging.Notification(
    #         title=title,
    #         body=msg,
    #         image = image
    #     ),
    #     data=dataObject,
    #     tokens=registration_token
    #     # tokens=['jidjcnnckdnkn'],
    # )

    # response = messaging.send_multicast(message)

    messageObject = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=msg,
            image = image
        ),
        data=dataObject,
        topic="BitTalk"
        # token="fnclq8tQZ0cLrVjxokDvZh:APA91bGhcEBsJxOfMHLGIGs6y4WsdvEqsCy3_vrmuh2qCRXL4ae2ipmCqwUnGwdoJgn-WXz9eVlC1bpZrZpgom-dfNUMlPD7edLG_-UyMZgrSlZHNQVXlYuqae9-LBn7kcN-nKYOC8Fh",
    )

    response = messaging.send(message=messageObject)
    saveNotifications(title, msg, image)

    print('Successfully sent message:', response)
    return True

def saveNotifications(title, body, image):
    db = firestore.client()
    doc_ref  = db.collection('public_notifications').document(str(uuid.uuid4()))
    doc_ref.set({
        'title' : title,
        'body' : body,
        'notification_date' : datetime.today(),
        'image' : image
    })

def getNotificationsFromFCM():
    notifications = []
    db = firestore.client()
    docs = db.collection('public_notifications').order_by('notification_date', direction=firestore.Query.DESCENDING).stream()
    for doc in docs:
        notifications.append(doc.to_dict())
    return notifications
        