from django.db import models
from choice.models import Choice
from question.models import Question

class Certification(models.Model):
    enrollment_id = models.ForeignKey(
        'enrollment.Enrollment',
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return str(self.enrollment_id)

    @classmethod
    def create(cls, enrollment_id):
        certification = cls(enrollment_id=enrollment_id)
        certification.save()
        return certification

    @classmethod
    def is_elligible_for_certification(cls, request):
        course_id = request.GET['course_id']
        count_correct_answers = 0
        for question_id, choice_id in request.GET.items():
            if question_id != 'course_id':
                if Choice.objects.filter(id=choice_id).exists() and Choice.objects.get(id=choice_id).is_correct:
                    count_correct_answers += 1
        count_total_questions = len(Question.objects.filter(course_id=course_id))
        if count_correct_answers/count_total_questions > 0.5:
            return True
        return False
