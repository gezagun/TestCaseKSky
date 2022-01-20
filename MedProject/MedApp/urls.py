from django.urls import path
from .views import PatientList, PatientView, TreatmentCaseView, TreatmentsCaseList, DocumentBodyView


urlpatterns = [
    path('patients/', PatientList.as_view(), name='patients_list'),
    path('patients/<int:pk>', PatientView.as_view(), name='patient_detail'),
    path('treatments/', TreatmentsCaseList.as_view(), name='treatment_cases'),
    path('treatments/<int:pk>', TreatmentCaseView.as_view(), name='treatment_case_detail'),
    path('documents/', DocumentBodyView.as_view(), name='document_body'),

]