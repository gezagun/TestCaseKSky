from rest_framework import serializers
from .models import Patient, TreatmentCase, MedDocument, DocumentBody


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'fio', 'birthday_date', 'gender']


class MedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedDocument
        fields = ['header']


class TreatmentCaseSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField()  # для отображения не id пациента, а его ФИО, сработает, только если в
    # самой модели прописан спец.метод __str__ (взято из документации)

    documents = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TreatmentCase
        fields = ['id', 'patient', 'start_date', 'end_date', 'result', 'documents']


class DocumentBodySerializer(serializers.ModelSerializer):
    document = serializers.StringRelatedField()

    class Meta:
        model = DocumentBody
        fields = ['document']
