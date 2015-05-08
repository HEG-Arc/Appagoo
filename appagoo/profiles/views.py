from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from apps.models import Application
from users.models import User
from models import Profile, Threat, UserProfile
from serializers import ProfileSerializer, ThreatSerializer, UserProfileSerializer


class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):
        if request.POST:
            user = request.POST['user']
            applications = request.POST['applications'].split(',')
            userProfile = UserProfile.objects.get(user=User.objects.get(username=user))
            for app in applications:
                application = Application.objects.get(package=app)
                userProfile.installed.add(application)
                userProfile.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Applications could not be submitted.'
        }, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
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

