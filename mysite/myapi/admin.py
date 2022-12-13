from django.contrib import admin
from .models import Channel
from .models import Content

# Register your models here.
admin.site.register(Channel)
admin.site.register(Content)