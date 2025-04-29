from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from users.models import CustomUser


from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


# admin.site.unregister(User)
# admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin, ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


admin.site.register(CustomUser, CustomUserAdmin)
