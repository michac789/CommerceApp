from django.contrib import admin
from django.db.models.functions import Lower
from django.forms import Textarea
from .models import User, AdminPost


class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "tier")
    
    def get_ordering(self, _):
        return [Lower('username')]
    

class AdminPostConfig(admin.ModelAdmin):
    list_display = ("__str__", "creator", "time_created")
    formfield_overrides = {
        AdminPost.markdown: {'widget': Textarea(attrs = {
            'rows': 4, 'cols': 40})},
    }


admin.site.register(User, UserAdmin)
admin.site.register(AdminPost, AdminPostConfig)
