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
        "email",
        "first_name",
        "city",
        "age",
        "role",
    )
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'city', 'age')}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'city', 'age'),
        }),
    )
    
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'city')
    
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
