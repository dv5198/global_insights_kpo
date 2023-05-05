from django.contrib import admin

from new_project.models import User_Details, Warranty_Details
from django.contrib.auth.models import Group

admin.site.unregister(Group)


# ------------------USER MODEL-------------------------
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "name", "phone_no", "email")
    list_display_links = (
        "id",
        "name",
    )


admin.site.register(User_Details, UserAdmin)


class WarrantyAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "model_number",
        "serial_number",
        "purchase_date",
        "purchase_place",
        "warranty_date",
        "delivery_order",
    )
    list_display_links = (
        "user",
        "product",
    )


admin.site.register(Warranty_Details)
