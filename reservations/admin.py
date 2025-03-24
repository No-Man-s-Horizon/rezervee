from django.contrib import admin
from reservations.models import Reservation, Vendor, Customer


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reservation._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at"]

    class Meta:
        model = Reservation


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vendor._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at"]

    class Meta:
        model = Vendor


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at"]

    class Meta:
        model = Customer
