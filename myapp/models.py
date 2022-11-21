from django.db import models
from django.contrib.auth.models import User


GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_OTHER = 'other'
GENDER_NOT_SPECIFIED = 'not specified'
GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
    (GENDER_OTHER, 'Other'),
    (GENDER_NOT_SPECIFIED, 'Not specified'),
)


class User_Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='',
                             blank=True, unique=True)
    about_me = models.TextField(blank=True, default='', max_length=10000)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=32, choices=GENDER_CHOICES, default=GENDER_NOT_SPECIFIED)
    profile_picture = models.ImageField(
        blank=True, null=True, upload_to='image')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
