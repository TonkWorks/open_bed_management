from django.db import models
from django.conf import settings
from dry_rest_permissions.generics import DRYPermissions


class Status(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=255, default='label label-info', blank=True)
    icon = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return False
        
    def has_object_read_permission(self, request):
        return True

    def has_object_write_permission(self, request):
        return False

class Tag(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=255, default='label label-info', blank=True)
    icon = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return False

    def has_object_read_permission(self, request):
        return True

    def has_object_write_permission(self, request):
        return False

class Bed(models.Model):
    name = models.CharField(max_length=255, default='Bed')
    status = models.ForeignKey(Status, default=0)
    room = models.CharField(max_length=255, default='')
    tags = models.ManyToManyField(Tag, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        if request.user.is_authenticated():
            return True
        return False

    def has_object_write_permission(self, request):
        if request.user.is_authenticated():
            return True
        else:
            return False

    @staticmethod
    def has_update_permission(request):
        if request.user.is_authenticated():
            return True
        return False

    def has_object_update_permission(self, request):
        if request.user.is_authenticated():
            return True
        else:
            return False

    def has_object_destroy_permission(self, request):
        if request.user.is_authenticated():
            return True
        else:
            return False

class AlertRule(models.Model):
    alert_rule = models.TextField(default="{}")

    @staticmethod
    def has_read_permission(request):
        return True
    def has_object_read_permission(self, request):
        return True
    @staticmethod
    def has_write_permission(request):
        return False

    def has_object_write_permission(self, request):
        return False


class Log(models.Model):
    subject = models.ForeignKey(Bed)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    time = models.DateTimeField(auto_now=True)
    log = models.TextField(default="{}")

    @staticmethod
    def has_read_permission(request):
        return True
    def has_object_read_permission(self, request):
        return True
    @staticmethod
    def has_write_permission(request):
        return False

    def has_object_write_permission(self, request):
        return False

