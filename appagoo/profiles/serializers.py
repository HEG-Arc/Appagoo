from models import Application
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='email'
    )

    threat = serializers.SlugRelatedField(
        read_only=True,
        slug_field='label'
    )

    class Meta:
        model = Application
        fields = ('id', 'user', 'threat', 'value')


class ThreatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'label', 'default_value')