# -*- coding: utf-8 -*-
# Import the reverse lookup function
import json
from urllib import urlopen
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp, SocialLogin
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from rest_framework import viewsets, permissions, status, views
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from profiles.models import UserProfile, Profile, Threat
from permissions import IsAccountOwner
from serializers import UserSerializer
from .forms import UserForm

# Import the customized User model
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


# ViewSets define the view behavior.
class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        if request.user.is_authenticated():
            queryset = User.objects.get(username=request.user)
            serializer = UserSerializer(queryset, context={'request': request})
            return Response(serializer.data)
        else:
            return Response()


'''
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            userProfile = UserProfile.objects.create(user=user)
            for threat in Threat.objects.all():
                Profile.objects.create(userProfile=userProfile, threat=threat, value=5)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    permission_classes = []

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                print("User is valid, active and authenticated")
                login(request, user)
                serialized = UserSerializer(user, context={'request': request})

                return Response(serialized.data)
            else:
                print("The password is valid, but the account has been disabled!")
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LoginTokenView(views.APIView):
    permission_classes = []

    def post(self, request, format=None):
        data = json.loads(request.body)
        access_token = data.get('access_token', None)

        url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token="+access_token
        google_data = json.loads(str(urlopen(url).read()))

        if google_data['issued_to']:
            email = google_data.get('email', None)
            uid = google_data.get('user_id', None)
            userExists = User.objects.filter(username=email).count()
            print 'userExists ----->'
            print userExists
            if userExists > 0:
                user = User.objects.get(username=email)
                user.backend = "allauth.account.auth_backends.AuthenticationBackend"
                login(request, user)
                serialized = UserSerializer(user, context={'request': request})
                print('user authenticated?')
                print(user.is_authenticated())
                return Response(serialized.data)
            else:
                user = User.objects.create_user(username=email, email=email, password=None)
                user.backend = "allauth.account.auth_backends.AuthenticationBackend"
                user.save()
                userProfile = UserProfile.objects.create(user=user)
                for threat in Threat.objects.all():
                    Profile.objects.create(userProfile=userProfile, threat=threat, value=5)
                sa = SocialAccount.objects.create(user=user, provider='google', uid=uid, extra_data=google_data)
                sa.save()
                token = SocialToken.objects.create(app=SocialApp.objects.get(provider='google'), account=sa, token=access_token)
                token.save()
                login(request, user)
                serialized = UserSerializer(user, context={'request': request})
                return Response(serialized.data)
        elif google_data['error']:
            return Response({
                'status': 'Unauthorized',
                'message': 'Invalid Google access token.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = []

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)
'''

