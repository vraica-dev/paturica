from collections.abc import Iterable
from django.db import models


class HandMadePic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, default="Handmade Object")
    pic_obj = models.ImageField(upload_to='images/')
    in_carousel = models.BooleanField(default=False)


class ContactMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(max_length=2500, blank=False, null=False)


class Produs(models.Model):
    id = models.AutoField(primary_key=True)
    pic = models.ForeignKey(HandMadePic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=400)
    info = models.TextField(max_length=800)
    

