from django.urls import path
from .views import PatientList, PatientView, TreatmentCaseList, TreatmentCaseView, TreatmentsCaseList


urlpatterns = [
    path('patients/', PatientList.as_view(), name='patients_list'),
    path('patients/<int:pk>', PatientView.as_view(), name='patient_detail'),
    path('treatments/', TreatmentsCaseList.as_view(), name='treatment_cases'),
    path('treatments/<int:pk>', TreatmentCaseView.as_view(), name='treatment_case_detail'),


]