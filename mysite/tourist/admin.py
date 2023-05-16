from django.contrib import admin
from .models import Clients, Seasons, Tours, Trips

# admin.site.register(Clients)
# admin.site.register(Seasons)
# admin.site.register(Tours)
# admin.site.register(Trips)


class TripsInline(admin.TabularInline):
    model = Trips

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'middle_name', 'last_name')
    fields = ['name', 'last_name', ('middle_name', 'passport')]
    inlines = [TripsInline]

class SeasonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end', 'closed')
    list_filter = ('id', 'closed')

class ToursAdmin(admin.ModelAdmin):
    list_display = ('id', 'season_id', 'name', 'info', 'price')
    fieldsets = (
        (None, {
            'fields': ('id', 'season_id')
        }),
        ('Info', {
            'fields': ('name', 'info', 'price')
        }),
    )


admin.site.register(Clients,ClientsAdmin)
admin.site.register(Seasons,SeasonsAdmin)
admin.site.register(Tours,ToursAdmin)
admin.site.register(Trips)





