import json
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from apps.models import Application
from users.models import User
from apps.serializers import ApplicationSerializer
from models import Profile, Threat, UserProfile
from serializers import ProfileSerializer, ThreatSerializer, UserProfileSerializer


class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def list(self, request):
        if request.user.is_authenticated():
            try:
                userprofile = UserProfile.objects.get(user=request.user)
                queryset = Application.objects.filter(userprofile=userprofile)
                if 'profile' in request.GET:
                    profile = request.GET['profile'].split(',')
                    queryset = queryset.extra(select={'score': "threat_location*"+profile[0]+"+threat_system*"+profile[1]+"+threat_profil*"+profile[2]+"+threat_social*"+profile[3]+"+threat_interests*"+profile[4]+"+threat_calendar*"+profile[5]+"+threat_media*"+profile[6]})
                    queryset = queryset.order_by('-score')
            except UserProfile.DoesNotExist:
                queryset = None
            if queryset is not None:
                serializer = ApplicationSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return Response({
                    'status': 'Unknown userprofile!',
                    'message': 'User has no user userprofile on appagoo.com.'
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': 'Not authenticated!',
                'message': 'Applications could not be submitted.'
            }, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request):
        if request.body:
            data = json.loads(request.body)
            user = data.get('user', None)
            applications = data.get('applications', None).split(',')
            try:
                userProfile = UserProfile.objects.get(user=User.objects.get(username=user))
            except User.DoesNotExist:
                userProfile = None
            if userProfile is not None:
                for app in applications:
                    try:
                        application = Application.objects.get(package=app)
                    except Application.DoesNotExist:
                        application = None
                    if application != None:
                        userProfile.installed.add(application)
                    userProfile.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'Unknown user!',
                    'message': user + ' has no account on appagoo.com.'
                }, status=status.HTTP_202_ACCEPTED)
        return Response({
            'status': 'Bad request',
            'message': 'Applications could not be submitted.'
        }, status=status.HTTP_400_BAD_REQUEST)



class ProfileViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        if request.user.is_authenticated():
            queryset = Profile.objects.filter(userProfile=UserProfile.objects.get(user=request.user)).order_by('id')
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

