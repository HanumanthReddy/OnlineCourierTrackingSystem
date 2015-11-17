from django.db import models
from mainadmin.models import UserProfile

class Parcel_Data(models.Model):

    C_ID = models.ForeignKey(UserProfile,default='C0001')
    P_ID = models.CharField(max_length='128')
    P_Date = models.DateField(default='2015-06-06')
    P_Source = models.CharField(max_length='128')
    P_Destination = models.CharField(max_length='128')
    P_A_Time = models.DateTimeField(auto_now_add = True, auto_now = False)
    P_D_Time = models.DateTimeField(auto_now_add = True, auto_now = False)
    P_Last = models.CharField(max_length='128')
    P_Next = models.CharField(max_length='128')
    P_Status = models.CharField(max_length='128', choices=[('In_Transit', 'In_Transit'), ('Delivered', 'Delivered'),('Cancelled', 'Cancelled')])

    def __str__(self):
        return str(self.P_ID)
# Create your models here.


class online_data(models.Model):

    ptype = models.CharField(max_length=128)
    pweight = models.CharField(max_length=128)
    pmail = models.CharField(max_length=128)
    paddress = models.CharField(max_length=128)
    pmobile = models.CharField(max_length=128)

    def __str__(self):
        return str(self.ptype)