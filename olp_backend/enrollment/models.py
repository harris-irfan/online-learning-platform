from django.db import models
from django.contrib.auth.models import User

class Enrollment(models.Model):
    course_id = models.ForeignKey(
        'course.Course',
        on_delete = models.CASCADE,
    )
    student_id = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return str(self.course_id) + ": " + str(self.student_id)

    @classmethod
    def create(cls, course_id, student_id):
        enrollment = cls(course_id=course_id, student_id=student_id)
        enrollment.save()
        return enrollment
