from django.contrib import admin
from . models import Hotels,Booking,Comment

# Register your models here.
admin.site.register(Hotels)
admin.site.register(Booking)
admin.site.register(Comment)