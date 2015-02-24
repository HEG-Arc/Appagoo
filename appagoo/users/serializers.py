from rest_framework import serializers
from models import User

__author__ = 'alessio'

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'first_name', 'last_name')