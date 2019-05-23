from django.contrib import admin

from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('date',)
    list_filter = ('date',)
    search_fields = ('Ce que vous Pensez de MrBot:',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
