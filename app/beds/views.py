import json

import rest_framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters

from dry_rest_permissions.generics import DRYPermissions

import django_filters

from django.conf import settings
from constance import config

from beds.models import Bed
from beds.models import Log
from beds.models import Tag
from beds.models import Status
from beds.models import AlertRule

from beds.filters import BedFilter
from beds.filters import LogFilter
from beds.filters import TagFilter
from beds.filters import StatusFilter

from beds.serializers import BedSerializer
from beds.serializers import LogSerializer
from beds.serializers import TagSerializer
from beds.serializers import StatusSerializer

from beds.alerts import AlertManager

class BedViewSet(viewsets.ModelViewSet):
    """Bed Information with Status and Tags"""
    permission_classes = (DRYPermissions, rest_framework.permissions.IsAuthenticated)
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    filter_class = BedFilter

    def get_queryset(self):
        return Bed.objects.all().prefetch_related('tags', 'status')

    def perform_update(self, serializer):
        """1. Capture a log entry for any updates to bed information through REST
           2. Follow Alert Rules to send out alerts.
        """

        # Capture a log entry for any updates to bed information through REST
        original_object = self.get_object()
        new_object = serializer.save()

        old = BedSerializer(original_object).data
        new = BedSerializer(new_object).data

        diff = {}
        for key in new.keys():
            if str(old[key]) != str(new[key]):
                diff[key] = new[key]

        Log.objects.create(
            subject = self.get_object(),
            user = self.request.user,
            log = json.dumps(diff))

        # Go Through Alert Rules to send out alerts.
        print(new_object)
        AlertManager().run(obj=new_object, diff=diff)



    # # #Override here to set owner
    # def perform_create(self, serializer):
    #     print("AAAAA")
    #     serializer.save(owner=self.request.user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # @list_route(methods=['post'])
    # def make(self, request):

    #     a = Address(
    #         name = request.data.get('name', None),
    #         line1 = request.data.get('line1', None),
    #         line2 = request.data.get('line2', None),
    #         city = request.data.get('city', None),
    #         state = request.data.get('state', None),
    #         postal_code = request.data.get('postal_code', None),
    #         owner = self.request.user
    #     ).save()

    #     r = {
    #         'success': True,
    #     }
    #     return Response(r)


class LogViewSet(viewsets.ModelViewSet):
    """Logs of Bed Information/Status Changes"""
    permission_classes = (DRYPermissions, rest_framework.permissions.IsAuthenticated)
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_class = LogFilter

    def get_queryset(self):
        return Log.objects.all()

class TagViewSet(viewsets.ModelViewSet):
    """Bed Tag Information"""
    permission_classes = (DRYPermissions,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_class = TagFilter

    def get_queryset(self):
        return Tag.objects.all()

class StatusViewSet(viewsets.ModelViewSet):
    """Status Tag Information"""
    permission_classes = (DRYPermissions, rest_framework.permissions.IsAuthenticated)
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_class = StatusFilter

    def get_queryset(self):
        return Status.objects.all()

class SettingsViewSet(viewsets.ViewSet):
    """Sits settings information as well as all possible Tags and Statuses"""
    def list(self, request):
        # Gather All The Settings set in the Config
        settings_dictionary = {}
        for key in settings.CONSTANCE_CONFIG:
            settings_dictionary[key] = getattr(config, key)

        return Response({
            'settings': settings_dictionary,
            'tags': TagSerializer(Tag.objects.all(), many=True).data,
            'statuses': StatusSerializer(Status.objects.all(), many=True).data
        })
