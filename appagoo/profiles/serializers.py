from models import Profile, Threat, UserProfile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    threat = serializers.SlugRelatedField(
        read_only=True,
        slug_field='label'
    )

    class Meta:
        model = Profile
        fields = ('id', 'threat', 'value')


class ThreatSerializer(serializers.ModelSerializer):
    threat = serializers.SerializerMethodField('get_label')
    value = serializers.SerializerMethodField('get_default_value')

    class Meta:
        model = Threat
        fields = ('id', 'threat', 'value')

    def get_label(self, obj):
        return obj.label

    def get_default_value(self, obj):
        return obj.default_value