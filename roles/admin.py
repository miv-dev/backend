from django.contrib import admin

from roles.models import Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


admin.site.register(Role, RoleAdmin)
