from django.db import models
from django.contrib import admin
from redis import Redis


class Room(models.Model):
    room_name = models.CharField(max_length=20)
    announcement = models.TextField(default="None")


admin.site.register(Room)

rds = Redis()
