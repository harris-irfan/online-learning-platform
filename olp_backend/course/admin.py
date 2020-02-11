from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'duration', 'video_link')

admin.site.register(Course, CourseAdmin)
