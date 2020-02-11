from django.db import models


class Course(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1200)
    duration = models.CharField(max_length=50)
    video_link = models.CharField(max_length=300)
    content_html_path = models.CharField(max_length=300)

    def __str__(self):
        return self.name
