from django.contrib import admin
from .models import inscripcion

# Register your models here.
class InscripcionAdmin(admin.ModelAdmin):
    readonly_fields = ('updated','created')
    # list_filter = ('procedure', 'status')
    # list_display = ('name','procedure', 'status')


admin.site.register(inscripcion, InscripcionAdmin)