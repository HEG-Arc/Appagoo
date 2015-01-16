from django.db import models


class Permission(models.Model):
    label = models.CharField(max_length=500, blank=True, null=True)


class Family(models.Model):
    label = models.CharField(max_length=500, blank=True, null=True)


class Category(models.Model):
    label = models.CharField(max_length=500, blank=True, null=True)
    family = models.ForeignKey(Family, null=True)


class Downloads(models.Model):
    label = models.CharField(max_length=500, blank=True, null=True)


class Content(models.Model):
    label = models.CharField(max_length=500, blank=True, null=True)


class Language(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    label = models.CharField(max_length=500, blank=True, null=True)


class Application(models.Model):
    package = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    price = models.FloatField(null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    evaluation = models.FloatField(null=True)
    number_evaluations = models.BigIntegerField(null=True)
    developer = models.CharField(max_length=500, blank=True, null=True)
    iap = models.BooleanField(default=False)
    training = models.BooleanField(default=False)
    icon = models.CharField(max_length=500, blank=True, null=True)
    market_url = models.CharField(max_length=500, blank=True, null=True)
    permissions = models.ManyToManyField(Permission, null=True)
    category = models.ForeignKey(Category, null=True)
    content = models.ForeignKey(Content, null=True)
    downloads = models.ForeignKey(Downloads, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.package


class Description(models.Model):
    text = models.TextField(null=True)
    language = models.ForeignKey(Language, null=True)
    application = models.ForeignKey(Application, null=True)