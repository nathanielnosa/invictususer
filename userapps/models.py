from django.db import models
from django.contrib.auth.models import User

import uuid

GENDER_CHOICE = (
    ('male','Male'),
    ('female', 'Female')
)
class Profile(models.Model):
    id = models.UUIDField(unique=True,primary_key=True, default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,choices=GENDER_CHOICE)
    profile_pix = models.ImageField(upload_to='users-image/',default="https://www.shareicon.net/data/128x128/2016/07/26/802026_man_512x512.png", blank=True,null=True)
    bio = models.TextField(max_length=500, blank=True,null=True)

    def __str__(self):
        return self.username

