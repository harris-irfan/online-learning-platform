from rest_framework import viewsets
from question.models import Question
from choice.models import Choice
from rest_framework.decorators import api_view
from course.models import Course
from rest_framework.response import Response
from django.core import serializers
from django.http import HttpResponse
from itertools import chain
from certification.models import Certification
from enrollment.models import Enrollment
from django.db import models


@api_view(['GET',])
def question_view(request):
    data = {}
    if Question.objects.filter(course_id=request.GET['course_id']).exists():
        question_queryset = Question.objects.filter(course_id=request.GET['course_id'])
        questions = [question.id for question in question_queryset]
        # data['response'] = questions
        # return Response(data)
        choice_queryset = Choice.objects.filter(question_id__in = questions)
        #data = serializers.serialize('json', question_queryset)
        both = list(chain(question_queryset, choice_queryset))
        data = serializers.serialize('json', both)
        return HttpResponse(data, content_type="application/json")
    else:
        data['response'] = 'Course not found'
        return Response(data)

@api_view(['POST',])
def submit_view(request):
    data = {}
    if Certification.is_elligible_for_certification(request):
        enrollment = Enrollment.objects.get(course_id=request.GET['course_id'], student_id=request.user.id)
        enrollment_id = enrollment.id
        certification = Certification.create(enrollment)
        #data['credential_id'] = certification.id
        data['credential_id'] = Certification.objects.get(enrollment_id = enrollment_id).id
    else:
        data['response'] = 'You are not elligible for the certification'
    return Response(data)
