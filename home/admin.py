from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Feedback)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Information)