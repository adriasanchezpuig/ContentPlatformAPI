from django.contrib import admin
from .models import Channel, Content, Group

# Register your models here.
admin.site.register(Channel)
admin.site.register(Content)
admin.site.register(Group)