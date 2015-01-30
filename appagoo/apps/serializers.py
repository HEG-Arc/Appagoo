from models import Application
from rest_framework import serializers


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'price', 'currency', 'evaluation', 'number_evaluations', 'icon', 'market_url', 'downloads', 'category')


class DownloadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'rank', 'label')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'label')