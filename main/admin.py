from django.contrib import admin

from main.models import Client, Message, Mailing, Try

# Register your models here.

admin.site.register(Client)
admin.site.register(Message)
admin.site.register(Mailing)
admin.site.register(Try)
