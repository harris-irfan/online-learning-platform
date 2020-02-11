from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from course.models import Course
from rest_framework.response import Response
from rest_framework.decorators import api_view


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

@api_view(['GET',])
def course_content_view(request):
    data = {}
    if Course.objects.filter(id=request.GET['id']).exists():
        data['video_link'] = Course.objects.get(id=request.GET['id']).video_link
        data['content_html_path'] = Course.objects.get(id=request.GET['id']).content_html_path
    else:
        data['response'] = 'Course not found'

    return Response(data)

# @api_view(['POST',])
# def post_course_content_view(request):
#     data = {}
#     if Course.objects.filter(id=request.GET['id']).exists():
#         data['video_link'] = Course.objects.get(id=request.GET['id']).video_link
#         data['content_html_path'] = Course.objects.get(id=request.GET['id']).content_html_path
#     else:
#         data['response'] = 'Course not found'
#
#     return Response(data)
