from django.db import models


class Certification(models.Model):
    enrollment_id = models.ForeignKey(
        'enrollment.Enrollment',
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return str(self.course_id) + ": " + str(self.student_id)

    @classmethod
    def create(cls, course_id, student_id):
        certification = cls(enrollment_id=enrollment_id)
        return enrollment
