from django.contrib import admin

from .models import Certification


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('enrollment_id',)

admin.site.register(Certification, CertificationAdmin)
