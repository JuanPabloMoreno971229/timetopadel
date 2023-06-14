from django.contrib import admin
from .models import club, torneo

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    readonly_fields = ('updated','created')
    # list_filter = ('procedure', 'status')
    # list_display = ('name','procedure', 'status')

class TorneoAdmin(admin.ModelAdmin):
    readonly_fields = ('updated','created')
    # list_filter = ('procedure', 'status')
    # list_display = ('name','procedure', 'status')

admin.site.register(club, ClubAdmin)
admin.site.register(torneo, TorneoAdmin)