from django.urls import path
from core.views import VisitorRegistrationView, PractitionerRegistrationView

app_name = 'core'

urlpatterns = [
    #Registration Urls
    path('registration/visitor/', VisitorRegistrationView.as_view(), name='register-visitor'),
    path('registration/practitioner/', PractitionerRegistrationView.as_view(), name='register-practitioner'),
    
]