from django.contrib import admin

from .models import Candidate
from .utils import datetime_format_ist, truncated_uuid


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    def truncated_id(self):
        return truncated_uuid(self.id)

    truncated_id.admin_order_field = "id"
    truncated_id.short_description = "id"

    def created_at_ist(self):
        return datetime_format_ist(self.created_at)

    created_at_ist.admin_order_field = "created_at"
    created_at_ist.short_description = "Created at IST"

    def updated_at_ist(self):
        return datetime_format_ist(self.updated_at)

    updated_at_ist.admin_order_field = "updated_at"
    updated_at_ist.short_description = "Updated at IST"

    list_display = [
        truncated_id,
        "name",
        "age",
        "gender",
        "email",
        "phone_number",
        created_at_ist,
        updated_at_ist,
    ]
    list_filter = [
        "gender",
    ]
    search_fields = [
        "id",
        "name",
        "email",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
