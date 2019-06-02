from django.contrib import admin
from .models import UserInfo, AuthToken

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(AuthToken)
