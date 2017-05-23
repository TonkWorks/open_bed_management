from django.contrib import admin
from rest_framework.authtoken.models import Token

from beds.models import Status
from beds.models import Tag
from beds.models import Bed
from beds.models import AlertRule

class StatusAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class BedAdmin(admin.ModelAdmin):
    pass

class AlertRuleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status, StatusAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Bed, BedAdmin)
admin.site.register(AlertRule, AlertRuleAdmin)

admin.site.unregister(Token)
