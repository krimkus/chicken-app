from django.contrib import admin
from basic_models.admin import SlugModelAdmin, DefaultModelAdmin
from data.models import *


class CheckinTypeAdmin(SlugModelAdmin):
    pass

admin.site.register(CheckinType, CheckinTypeAdmin)


class CheckinAdmin(DefaultModelAdmin):
    list_display = ('checkintype',)

admin.site.register(Checkin, CheckinAdmin)
