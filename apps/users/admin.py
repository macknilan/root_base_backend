from django.contrib import admin

# Register your models here.
"""User models admin."""

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from apps.users.forms import UserAdminChangeForm, UserAdminCreationForm

# Models
from apps.users.models import User, Profile

# User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    fieldsets = (
        (_("User"), {"fields": ("is_verified", "is_public")}),
    ) + auth_admin.UserAdmin.fieldsets
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_superuser",
        "is_verified",
        "is_public",
    ]
    search_fields = ["username", "email"]


@admin.register(Profile)
class UserProfile(admin.ModelAdmin):
    """Profile model admin"""

    # def picture_tag(self, obj):
    #     return format_html(
    #         '<img src="{}" style="max-width:150px; max-height:150px"/>'.format(
    #             obj.picture.url
    #         )
    #     )

    list_display = ("user", "biography", "picture")
    search_fields = (
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    fieldsets = [
        (
            _("Profile"),
            {
                "fields": (("user", "biography", "picture"),),
            },
        ),
        (
            _("Metadata"),
            {
                "fields": (("created", "modified"),),
            },
        ),
    ]
    readonly_fields = (
        "created",
        "modified",
    )


# admin.site.register(User, UserAdmin)
