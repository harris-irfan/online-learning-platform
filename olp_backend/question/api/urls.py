from django.urls import path, include
from question.api.views import(
    question_view,
    submit_view
)

app_name = 'question'

urlpatterns = [
        path('', question_view, name='questions'),
        path('submit/', submit_view, name='submit_quiz')
]
