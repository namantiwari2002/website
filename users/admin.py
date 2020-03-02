from django.contrib import admin
from .models import Profile, Address


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_merchant', 'department', 'club', 'batch']
    list_editable = ['is_merchant', 'department', 'club', 'batch']


admin.site.register(Profile, ProfileAdmin)

admin.site.register(Address)