from django.db import models

from question.models import Question


class Choice(models.Model):
    text = models.CharField(max_length=500)
    question_id = models.ForeignKey(
        'question.Question',
        on_delete = models.CASCADE,
    )
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text
