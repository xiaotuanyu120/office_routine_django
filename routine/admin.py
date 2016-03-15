from django.contrib import admin

from .forms import RoutineTaskForm
from .models import RoutineTask


class RoutineTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'create_by', 'assigned_to', 'create_time', 'update_time')
    form = RoutineTaskForm
    #class Meta:
    #    model = RoutineTask


admin.site.register(RoutineTask, RoutineTaskAdmin)
