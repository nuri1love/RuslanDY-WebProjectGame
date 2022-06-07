from django.contrib import admin
from .models import Skill, Enemy, Thing, Location
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Skill)
class skils(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Enemy)
class enemys(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Thing)
class things(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Location)
class locs(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
