from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'created_at',
    )
    exclude = (
        'id',
    )

    def status(self, obj):
        return obj.status

    status.short_description = 'Статус'
