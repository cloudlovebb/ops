from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible

from django.conf import settings


@python_2_unicode_compatible
class Ip(models.Model):
    """
    IP地址
    """
    ip = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip


@python_2_unicode_compatible
class Server(models.Model):
    """
    服务器
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Business(models.Model):
    """
    业务线
    """
    business_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


@python_2_unicode_compatible
class Project(models.Model):
    """
    项目
    """
    project_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


@python_2_unicode_compatible
class Service(models.Model):
    """
    应用服务
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
