from rest_framework import status, generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient, TreatmentCase
from .serializers import PatientSerializer, TreatmentCaseSerializer


class PatientList(APIView):
    """Просмотр всех клиентов на одной странице (пагинация не предусмотрена)"""

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PatientView(APIView):
    """Детальный просмотр клиента по его pk (primary key = id)"""

    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = Patient.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TreatmentsCaseList(generics.GenericAPIView, CreateModelMixin, ListModelMixin):
    """Просмотр всех случаев лечения на одной странице (пагинация не предусмотрена)"""

    serializer_class = TreatmentCaseSerializer

    def get_queryset(self):
        queryset = TreatmentCase.objects.all()
        treatment_name = self.request.query_params.get('patient')
        if treatment_name:
            queryset = queryset.filter(patient=treatment_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class TreatmentCaseList(APIView):
    """Просмотр всех случаев лечения на одной странице (пагинация не предусмотрена)"""

    def get(self, request):
        treatment_cases = TreatmentCase.objects.all()
        serializer = TreatmentCaseSerializer(treatment_cases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TreatmentCaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TreatmentCaseView(APIView):
    """Просмотр детального случая лечения по его id (pk = id)"""

    def get_object(self, pk):
        try:
            return TreatmentCase.objects.get(pk=pk)
        except TreatmentCase.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        treatment = self.get_object(pk)
        serializer = TreatmentCaseSerializer(treatment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        treatment = TreatmentCase.get_object(pk)
        serializer = TreatmentCaseSerializer(treatment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)