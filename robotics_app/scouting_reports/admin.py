from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ScoutingReport, OpposingTeam

# Register your models here.
admin.site.register(ScoutingReport, UserAdmin)
admin.site.register(OpposingTeam, UserAdmin)

# Register your models here.
