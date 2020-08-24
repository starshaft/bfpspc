from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('analytics/', analytics, name='analytics'),
    path('incident_datasets/', incident_datasets, name="incident_datasets"),
    path('barangay_incident_count/', barangay_incident_count, name='barangay_incident_count'),
]
