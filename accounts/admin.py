from django.contrib import admin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_display_links = ["bio"]
    search_fields = ["bio"]
    list_filter = ["created_at"]

    class Meta:
        model = Profile
