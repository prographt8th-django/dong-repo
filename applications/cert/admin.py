from django.contrib import admin

# Register your models here.
from applications.cert.models import University, User

admin.site.register(University)
admin.site.register(User)
