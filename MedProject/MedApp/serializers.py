from rest_framework import serializers
from .models import Patient, TreatmentCase, MedDocument


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'fio', 'birthday_date', 'gender']


class TreatmentCaseSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField()  # для отображения не id пациента, а его ФИО, сработает, только если в
    # самой модели прописан спец.метод __str__ (взято из документации)

    class Meta:
        model = TreatmentCase
        fields = ['id', 'patient', 'start_date', 'end_date', 'result']
