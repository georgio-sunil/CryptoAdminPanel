from datetime import datetime
import firebase_admin
from firebase_admin import credentials, messaging, firestore

cred = credentials.Certificate("utilities/credentials/wm-notifications-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

def sendPush(title, msg, image, registration_token, dataObject=None):
    
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg,
            image = image
        ),
        data=dataObject,
        tokens=registration_token,
    )

    response = messaging.send_multicast(message)
    # print(response.failure_count)
    # print(response.responses[0].exception)
    # print(response.success_count)
    print('Successfully sent message:', response)