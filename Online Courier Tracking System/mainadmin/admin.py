from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from mainadmin.models import UserProfile

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class MyUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
