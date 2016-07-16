from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
