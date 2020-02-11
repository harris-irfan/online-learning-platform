from django.contrib import admin

from .models import Choice


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'is_correct', 'question_id')

admin.site.register(Choice, ChoiceAdmin)
