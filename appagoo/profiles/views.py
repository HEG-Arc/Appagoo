from docutils.nodes import status
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from models import Profile, Threat, UserProfile
from serializers import ProfileSerializer, ThreatSerializer


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        print 'request.user ----------> '
        print request.user
        if request.user.is_authenticated():
            queryset = Profile.objects.filter(userProfile=UserProfile.objects.get(user=request.user))
            serializer = ProfileSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Threat.objects.all()
            serializer = ThreatSerializer(queryset, many=True)
            return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Profile.objects.filter(userProfile=UserProfile.objects.get(user=request.user))
        profile = get_object_or_404(queryset, pk=pk)
        profile.value = request.data['value']
        profile.save()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer

