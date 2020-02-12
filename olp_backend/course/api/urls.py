from django.urls import path, include
from course.api.views import(
    CourseView,
    course_content_view
    enroll_view
)

app_name = 'course'

urlpatterns = [
        path('', CourseView.as_view({'get': 'list'}), name='courses'),
        path('enroll', enroll_view, name='enroll')
#        path('content/', course_content_view.as_view({'get': 'list'}), name='courses_content')
]
