from models import Profile, Threat, UserProfile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'userProfile', 'threat', 'value')


class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ('id', 'label', 'default_value')