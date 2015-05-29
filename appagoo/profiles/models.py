from django.db import models
from apps.models import Application, Permission
from users.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='profile')
    installed = models.ManyToManyField(Application, null=True)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'


class Threat(models.Model):
    label = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    default_value = models.IntegerField(null=True)
    permissions = models.ManyToManyField(Permission, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.label


class Profile(models.Model):
    userProfile = models.ForeignKey(UserProfile, null=True)
    threat = models.ForeignKey(Threat, null=True)
    value = models.IntegerField(null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.userProfile.user.username






