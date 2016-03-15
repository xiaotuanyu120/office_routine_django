from __future__ import unicode_literals

from django.db import models
from crum import get_current_user


class RoutineTask(models.Model):
    task = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    create_by = models.ForeignKey('auth.User', blank=True, null=True,
                                    default=None, related_name='+')
    assigned_to = models.ForeignKey('auth.User', blank=True, null=True,
                                    default=None, related_name='+')

    def save(self, *args, **kwargs):
        self.create_by = get_current_user()
        super(RoutineTask, self).save(*args, **kwargs)
