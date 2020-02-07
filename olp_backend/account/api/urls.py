from django.urls import path, include
from account.api.views import(
    registration_view,
)

app_name = 'account'

urlpatterns = [
        path('register', registration_view, name='register'),
        path('rest-auth/', include('rest_auth.urls')),
]
