from django.contrib import admin

from .models import Enrollment


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'student_id')

admin.site.register(Enrollment, EnrollmentAdmin)
