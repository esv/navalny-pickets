from django.contrib import admin

from picket.models import Picket, Organizer

class PicketAdmin(admin.ModelAdmin):
    pass

class OrganizerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Picket, PicketAdmin)
admin.site.register(Organizer, OrganizerAdmin)