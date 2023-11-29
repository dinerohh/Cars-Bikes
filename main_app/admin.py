from django.contrib import admin

from main_app.models import Team

# Register your models here.
admin.site.site_header = "Dinero Bikes"
admin.site.index_title = "Dinero Bikes"


class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "dob", "position"]
    search_fields = ["name", "email", "position"]


admin.site.register(Team, TeamAdmin)
