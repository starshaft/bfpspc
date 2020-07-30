from django.contrib import admin
from .models import Barangay, InvestigatorRank, Investigator, Incident, OccupancyType

@admin.register(Barangay)
class BarangayAdmin(admin.ModelAdmin):
    list_display = ('Name',)

@admin.register(InvestigatorRank)
class InvestigatorRankAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Definition',)
    
@admin.register(Investigator)
class InvestigatorAdmin(admin.ModelAdmin):
    list_display = ('Rank', 'LastName', 'FirstName',)

@admin.register(OccupancyType)
class OccupancyTypeAdmin(admin.ModelAdmin):
    list_display = ('Description', )

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('DateTime', 'HouseNumber', 'Street', 'Barangay', 'OwnerEstablishmentName',)
    exclude = ('TotalFatalities',)