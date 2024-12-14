from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=2000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)  # Stockera le texte chiffré
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    is_encrypted = models.BooleanField(default=True)  # Indique si le message est chiffré
