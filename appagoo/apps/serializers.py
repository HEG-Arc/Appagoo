from models import Application, Downloads, Category
from rest_framework import serializers


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    downloads = serializers.SlugRelatedField(
        read_only=True,
        slug_field='rank'
    )

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='label'
    )

    score = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Application
        fields = ('id', 'name', 'price', 'currency', 'evaluation', 'number_evaluations', 'icon', 'market_url', 'downloads', 'category', 'score')


class DownloadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Downloads
        fields = ('id', 'rank', 'label')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')