from django.contrib import admin
from . import models
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    # to display the title of the note
    list_display = ('title',)
    pass

# enabling notes model at admin interface
admin.site.register(models.Notes, NotesAdmin)