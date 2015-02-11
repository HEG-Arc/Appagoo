from django.shortcuts import render
from rest_framework import viewsets
from appagoo.profiles.models import Profile, Threat
from appagoo.profiles.serializers import ProfileSerializer, ThreatSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer
