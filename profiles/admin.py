from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

    exlude = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
