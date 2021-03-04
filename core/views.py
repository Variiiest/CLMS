from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from core.serializers import (
    VisitorRegistrationSerializer, PractitionerRegistrationSerializer
    )

class VisitorRegistrationView(RegisterView):
    serializer_class = VisitorRegistrationSerializer


class PractitionerRegistrationView(RegisterView):
    serializer_class = PractitionerRegistrationSerializer