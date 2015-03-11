from models import Profile, Threat, UserProfile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    threat = serializers.SlugRelatedField(
        read_only=True,
        slug_field='label'
    )

    class Meta:
        model = Profile
        fields = ('threat', 'value')


class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ('id', 'label', 'default_value')
