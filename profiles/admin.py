from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

    exclude = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
