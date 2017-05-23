from django.contrib.auth import get_user_model

from rest_framework import serializers

from beds.models import Bed
from beds.models import Log
from beds.models import Status
from beds.models import Tag

import json
# Serializers define the API representation.
class BedSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(slug_field='name', queryset=Status.objects.all())
    tags = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Bed


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Status

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag

class LogSerializer(serializers.ModelSerializer):
    log = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='name', queryset=get_user_model().objects.all())
    subject = serializers.SlugRelatedField(slug_field='name', queryset=Bed.objects.all())

    def get_log(self, obj):
        try:
            return json.loads(obj.log)
        except json.JSONDecodeError as e:
            pass
    class Meta:
        fields = '__all__'
        model = Log

