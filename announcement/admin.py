from django.contrib import admin

# Register your models here.
from .models import Announcement, comment
admin.site.register(Announcement)
admin.site.register(comment)
