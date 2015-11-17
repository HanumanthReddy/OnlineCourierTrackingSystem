from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    #user = models.OneToOneField(User,primary_key=True)
    user = models.OneToOneField(User, parent_link=True)
    C_ID = models.CharField(max_length= 128, primary_key=True, unique = True)
    C_Name = models.CharField(max_length  = 128, unique = True)

    def __str__(self):
        return str(self.C_ID)

# Create your models here.
