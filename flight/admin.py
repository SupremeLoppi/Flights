from django.contrib import admin
from .models import Cities,Airport,Flight

# Register your models here.

admin.site.register(Cities)
admin.site.register(Airport)
admin.site.register(Flight)

