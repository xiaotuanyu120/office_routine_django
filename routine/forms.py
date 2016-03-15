# coding:utf-8
from django import forms

from .models import RoutineTask
from crum import get_current_user


class RoutineTaskForm(forms.ModelForm):
    class Meta:
        model = RoutineTask
        #fields = ['task', 'create_by', 'assigned_to']
        fields = ['task', 'assigned_to']

    def clean_task(self):
        task = self.cleaned_data.get('task')
        if len(task) < 20:
            raise forms.ValidationError("任务长度：10-20字符")
        return task

    def clean_create_by(self):
        create_by = get_current_user()
        return create_by

    def clean_assigned_to(self):
        assigned_to = self.cleaned_data.get('assigned_to')
        if not assigned_to:
            raise forms.ValidationError("请选择任务执行人")
        return assigned_to
