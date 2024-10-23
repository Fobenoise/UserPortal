from django.contrib import admin
from .models import UserProfile, RoleProfile, Equipment

admin.site.register(UserProfile)
admin.site.register(RoleProfile)
admin.site.register(Equipment)
# Register your models here.
