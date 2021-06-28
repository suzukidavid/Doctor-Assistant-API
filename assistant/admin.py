from django.contrib import admin

from .models import (
    Patient,
    History,
    Investigation,
    Diagnosis,
    Surgery,
    FollowUp,
    DiseaseLibrary,
    InvestigationImage,
    InvestigationVideo,
    InvestigationDocument,
    SurgeryImage,
    SurgeryVideo,
    SurgeryDocument,
    FollowUpImage,
    FollowUpVideo,
    FollowUpDocument,

)

from django import forms


class PatientAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = [
        "name",
        "sex",
        "phone",
        "age",
        "assign_doctor",
        "date_of_admission",
        "date_of_discharge",
        "address",
        "professor_surgeon_consultant",
    ]
    readonly_fields = [

    ]
    search_fields = [
        'name',
        'phone',
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'assign_doctor', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Patient, PatientAdmin)

admin.site.register(DiseaseLibrary)
admin.site.register(History)


class InvestigationImageImageAdmin(admin.StackedInline):
    model = InvestigationImage


class InvestigationVideoAdmin(admin.StackedInline):
    model = InvestigationVideo


class InvestigationDocumentAdmin(admin.StackedInline):
    model = InvestigationDocument


@admin.register(Investigation)
class InvestigationAdmin(admin.ModelAdmin):
    inlines = [InvestigationImageImageAdmin, InvestigationVideoAdmin, InvestigationDocumentAdmin]

    class Meta:
        model = Investigation


admin.site.register(Diagnosis)


class SurgeryImageAdmin(admin.StackedInline):
    model = SurgeryImage


class SurgeryVideoAdmin(admin.StackedInline):
    model = SurgeryVideo


class SurgeryDocumentAdmin(admin.StackedInline):
    model = SurgeryDocument


@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    inlines = [SurgeryImageAdmin, SurgeryVideoAdmin, SurgeryDocumentAdmin]

    class Meta:
        model = Surgery


class FollowUpImageAdmin(admin.StackedInline):
    model = FollowUpImage


class FollowUpVideoAdmin(admin.StackedInline):
    model = FollowUpVideo


class FollowUpDocumentAdmin(admin.StackedInline):
    model = FollowUpDocument


@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):
    inlines = [FollowUpImageAdmin, FollowUpVideoAdmin, FollowUpDocumentAdmin]

    class Meta:
        model = FollowUp

