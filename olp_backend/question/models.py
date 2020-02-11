from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=1000)
    course_id = models.ForeignKey(
        'course.Course',
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.text
