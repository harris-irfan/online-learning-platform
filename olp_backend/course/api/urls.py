from django.urls import path, include
from course.api.views import(
    CourseView,
    course_content_view,
    enrollment_view
)

app_name = 'course'

urlpatterns = [
        path('', CourseView.as_view({'get': 'list'}), name='courses'),
        path('content/', course_content_view, name='course_content'),
        path('enrollment/', enrollment_view, name='enroll')
]
