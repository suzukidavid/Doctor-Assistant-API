from rest_framework import serializers
from account.models import User
from account.serializers import UserSerializer
from . import models
import base64


# # from drf_extra_fields.fields import Base64ImageField
# class Base64ImageField(serializers.ImageField):
#     def from_native(self, data):
#         if isinstance(data, basestring) and data.startswith('data:image'):
#             # base64 encoded image - decode
#             format, imgstr = data.split(';base64,')  # format ~= data:image/X,
#             ext = format.split('/')[-1]  # guess file extension
#
#             data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
#
#         return super(Base64ImageField, self).from_native(data)


class PatientSerializer(serializers.ModelSerializer):
    assign_doctor = UserSerializer(read_only=True)
    assign_doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assign_doctor', write_only=True)

    # profile_image = Base64ImageField(required=True)

    class Meta:
        model = models.Patient
        # fields = '__all__'
        fields = [
            "id",
            "registration_number",
            "profile_image",
            "name",
            "sex",
            "age",
            "phone",
            "address",
            "professor_surgeon_consultant",
            "assign_doctor",
            "assign_doctor_id",
            "date_of_discharge",
            "date_of_admission",
        ]


class DiseaseLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiseaseLibrary
        fields = '__all__'


class FamilyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FamilyHistory
        fields = '__all__'


class InvestigationSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(read_only=True)
    patients_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), source='patients', write_only=True)

    class Meta:
        model = models.Investigation
        fields = '__all__'


class SurgerySerializer(serializers.ModelSerializer):
    patients = PatientSerializer(read_only=True)
    patients_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), source='patients', write_only=True)

    class Meta:
        model = models.Surgery
        fields = '__all__'


class FollowUpSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(read_only=True)
    patients_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), source='patients', write_only=True)

    class Meta:
        model = models.FollowUp
        fields = '__all__'


class DiagnosisSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(read_only=True)
    patients_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), source='patients', write_only=True)

    class Meta:
        model = models.Diagnosis
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    patients = PatientSerializer(read_only=True)
    patients_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), source='patients', write_only=True)

    class Meta:
        model = models.History
        fields = '__all__'


"""
Media Serializer 

"""


class InvestigationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvestigationImage
        fields = '__all__'


class InvestigationVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvestigationVideo
        fields = '__all__'


class InvestigationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvestigationDocument
        fields = '__all__'


class SurgeryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurgeryImage
        fields = '__all__'


class SurgeryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurgeryVideo
        fields = '__all__'


class SurgeryDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurgeryDocument
        fields = '__all__'


class FollowUpImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FollowUpImage
        fields = '__all__'


class FollowUpVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FollowUpVideo
        fields = '__all__'


class FollowUpDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FollowUpDocument
        fields = '__all__'

# class PatientProfileSerializer(serializers.ModelSerializer):
#     categories_info = CategoriesInfoSerializer(read_only=True)
#     categories_info_id = serializers.PrimaryKeyRelatedField(
#         queryset=models.CategoriesInfo.objects.all(), source='categories_info', write_only=True)
#
#     class Meta:
#         model = models.Assign
#         fields = [
#             'categories_info',
#             'categories_info_id',
#             'specimen',
#             'investigation',
#             'referred_by',
#             'created_date',
#             'finishing_date'
#         ]
