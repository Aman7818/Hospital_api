from django.urls import path
from .views import doctor_register, doctor_login, patient_register, create_report, all_reports, reports_by_status

urlpatterns = [
    path('doctors/register', doctor_register),
    path('doctors/login', doctor_login),
    path('patients/register', patient_register),
    path('patients/<int:id>/create_report', create_report),
    path('patients/<int:id>/all_reports', all_reports),
    path('reports/<str:status>', reports_by_status),
]
