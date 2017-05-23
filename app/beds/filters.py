import django_filters

from beds.models import Bed
from beds.models import Log
from beds.models import Tag
from beds.models import Status

class BedFilter(django_filters.FilterSet):
    class Meta:
        model = Bed
        fields = '__all__'

class StatusFilter(django_filters.FilterSet):
    class Meta:
        model = Status
        fields = '__all__'

class TagFilter(django_filters.FilterSet):
    class Meta:
        model = Tag
        fields = '__all__'

class LogFilter(django_filters.FilterSet):
    class Meta:
        model = Log
        fields = '__all__'