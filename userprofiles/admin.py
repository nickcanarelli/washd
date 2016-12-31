from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    """ Details a person in line. """
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

    fields = ('user', 'is_client', 'is_washr', 'is_superuser', 'avatar', 'address', 'city', 'state', 'country')

class UserAdmin(UserAdmin):
    inlines = [
        ProfileInline
    ]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
