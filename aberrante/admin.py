from django.contrib import admin
from .models import Lead  # Import your custom model


admin.site.site_header = "Aberrante Admin Panel"  # Top-left header
admin.site.site_title = "Aberrante"  # Browser tab title
admin.site.index_title = "Bienvenido a Aberrante"  # Dashboard title

class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "type", "created_at") 
    readonly_fields = ("id", "created_at")

admin.site.register(Lead, LeadAdmin)
