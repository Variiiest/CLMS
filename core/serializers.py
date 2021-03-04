from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from core.models import Visitor, Practitioner



class VisitorRegistrationSerializer(RegisterSerializer):

    addressline1 = serializers.CharField(max_length=100)
    addressline2 = serializers.CharField(max_length=100)
    postal_code= serializers.IntegerField()
    city= serializers.CharField(max_length=100)
    state= serializers.CharField(max_length=100)
    country= serializers.CharField(max_length=100)
    gender = serializers.CharField(source='get_gender_display')
    dob = serializers.DateField()
    
    def get_cleaned_data(self):
            data = super(VisitorRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'addressline1' : self.validated_data.get('addressline1', ''),
                'addressline2' : self.validated_data.get('addressline2', ''),
                'postal_code': self.validated_data.get('postal_code', ''),
                'city' : self.validated_data.get('city', ''),
                'state' : self.validated_data.get('state', ''),
                'country': self.validated_data.get('country', ''),
                'gender' : self.validated_data.get('gender', ''),
                'dob': self.validated_data.get('dob', '')
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(VisitorRegistrationSerializer, self).save(request)
        user.is_visitor = True
        user.save()
        visitor = Visitor(visitor=user, addressline1=self.cleaned_data.get('addressline1'), 
                addressline2=self.cleaned_data.get('addressline2'),
                postal_code=self.cleaned_data.get('postal_code'), city= self.cleaned_data.get('city'), state=
                self.cleaned_data.get('state'), country= self.cleaned_data.get('country'), gender= self.cleaned_data.get('gender'),dob= self.cleaned_data.get('dob'))
        
        visitor.save()
        return user


class PractitionerRegistrationSerializer(RegisterSerializer):
    class Meta:
        model= Practitioner
        fields= '__all__'
    