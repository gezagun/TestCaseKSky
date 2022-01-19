from django.contrib import admin
from .models import Patient, TreatmentCase, MedDocument, DocumentBody
# Register your models here.


@admin.register(Patient)
class MedAppAdmin(admin.ModelAdmin):
    pass


@admin.register(TreatmentCase)
class MedAppAdmin(admin.ModelAdmin):
    pass


@admin.register(MedDocument)
class MedAppAdmin(admin.ModelAdmin):
    pass


@admin.register(DocumentBody)
class MedAppAdmin(admin.ModelAdmin):
    pass
