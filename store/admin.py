from django.contrib import admin
from models import cloud_users, items_cloud_d, bcc

admin.site.register(items_cloud_d)
admin.site.register(cloud_users)
admin.site.register(bcc)
