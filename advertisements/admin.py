from django.contrib import admin
from advertisements.models import Advertisement
from django.contrib.auth.models import User

# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#  pass

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
 pass


# admin.site.register(Advertisement, AdvertisementAdmin)
