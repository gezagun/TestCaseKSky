from django.urls import path
from .views import PatientList, PatientView


urlpatterns = [
    path('patients/', PatientList.as_view(), name='patients_list'),
    path('patients/<int:pk>', PatientView.as_view(), name='patient_detail')
]