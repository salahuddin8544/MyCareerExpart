import base64
import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    resume = models.FileField(upload_to='avatars/', null=True, blank=True)
    newsletter = models.BooleanField(default=False)

    usersecret = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.usersecret:
            self.usersecret = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
        super().save(*args, **kwargs)



class Interest(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_sector = models.CharField(max_length=255, null=True, blank=True)
    year_sector = models.CharField(max_length=255, null=True, blank=True)
    country_experience = models.CharField(max_length=255, null=True, blank=True)
    highest_degree = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    citizenship = models.CharField(max_length=255, null=True, blank=True)
    interested = models.ManyToManyField(Interest, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    linkedIn = models.CharField(max_length=50, null=True, blank=True)
    personal_email = models.CharField(max_length=50, null=True, blank=True)
    specializations = models.CharField(max_length=50, null=True, blank=True)
    
    def step_one_completed(self):
        return all([self.experience_sector, self.year_sector, self.country_experience, self.highest_degree])

    def step_two_completed(self):
        return all([self.language, self.gender, self.citizenship, self.interested.exists()])
    def __str__(self):
        return self.user.username