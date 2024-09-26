from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        if not change:
            obj.author = request.user
    
        super(TaskAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )