from django.contrib import admin

from .models import (
    Patient,
    CategoriesInfo,
    MediaVideo,
    MediaImage,
    MediaDocument,
    Assign
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
        "diagnosis",
        "sex",
        "phone",
        "age",
        "assign_doctor",
        "date_of_admission",
        "date_of_discharge",
        "address",
        "prof_surgeon_consultant",
    ]
    readonly_fields = [
        "date_of_admission",

    ]
    search_fields = [
        'name',
        'phone',
        'diagnosis',
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'assign_doctor', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Patient, PatientAdmin)


class CategoriesInfoAdminForm(forms.ModelForm):
    class Meta:
        model = CategoriesInfo
        fields = "__all__"


class CategoriesInfoAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = [
        'type',
        'type_name',
    ]


admin.site.register(CategoriesInfo, CategoriesInfoAdmin)


class PatientAssignAdminForm(forms.ModelForm):
    class Meta:
        model = CategoriesInfo
        fields = "__all__"


class PatientAssignAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = [
        'patient_id',
        'categories_info_id',
        'specimen',
        'investigation',
        'created_date',
        'finishing_date'
    ]


admin.site.register(Assign, PatientAssignAdmin)

admin.site.register(MediaVideo)
admin.site.register(MediaImage)
admin.site.register(MediaDocument)
