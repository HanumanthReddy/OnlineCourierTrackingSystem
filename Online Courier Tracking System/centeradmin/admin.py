from django.contrib import admin
from centeradmin.models import Parcel_Data
# Register your models here.
#
# P_ID = models.ForeignKey(Center_Data.C_ID)
# P_Name = models.ForeignKey(Center_Data.C_Name)
# P_Date = models.DateField(_("Date"), default=datetime.date.today)
# P_Source = models.CharField(max_length='128')
# P_Destination = models.CharField(max_length='128')
# P_A_Time = models.DateTimeField(auto_now_add = True, auto_now = False)
# P_D_Time = models.DateTimeField(auto_now_add = True, auto_now = False) + timedelta (hours = 2)
# P_Last = models.CharField(max_length='128')
# P_Next = models.CharField(max_length='128')
# P_Status = models.CharField(max_length='128')



class Parcel(admin.ModelAdmin):
    list_display = ['C_ID','P_ID', 'P_Date' ,'P_Source', 'P_Destination', 'P_A_Time', 'P_D_Time', 'P_Last', 'P_Next', 'P_Status']
    class Meta:
        model = Parcel_Data

admin.site.register(Parcel_Data, Parcel)

