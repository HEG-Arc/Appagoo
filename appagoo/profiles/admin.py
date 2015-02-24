from django.contrib import admin

# Register your models here.
from models import UserProfile, Threat, Profile

admin.site.register(UserProfile)
admin.site.register(Threat)
admin.site.register(Profile)
