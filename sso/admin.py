from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "tier")


admin.site.register(User, UserAdmin)
