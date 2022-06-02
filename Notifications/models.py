from django.db import models
from mongoengine import Document, fields
# Create your models here.

class Notifications(Document):
    title = fields.StringField(required=True)
    body = fields.StringField(required=True)
    notification_date = fields.DateTimeField()
    image = fields.StringField(required=True)

