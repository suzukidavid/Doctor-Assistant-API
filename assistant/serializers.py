from rest_framework import serializers
from account.models import User
from account.serializers import UserSerializer
from . import models


class PatientSerializer(serializers.ModelSerializer):
    assign_doctor = UserSerializer(read_only=True)
    assign_doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assign_doctor', write_only=True)

    class Meta:
        model = models.Patient
        # fields = '__all__'
        fields = [
            "name",
            "diagnosis",
            "sex",
            "age",
            "phone",
            "address",
            "prof_surgeon_consultant",
            "assign_doctor",
            "assign_doctor_id",
            "date_of_discharge",
            "date_of_admission",
        ]


class CategoriesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoriesInfo
        fields = '__all__'


class MediaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaImage
        fields = '__all__'


class MediaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaVideo
        fields = '__all__'


class MediaDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaDocument
        fields = '__all__'


class AssignSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(read_only=True)
    patients_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), source='patients', write_only=True)

    categories_info = CategoriesInfoSerializer(read_only=True)
    categories_info_id = serializers.PrimaryKeyRelatedField(
        queryset=models.CategoriesInfo.objects.all(), source='categories_info', write_only=True)

    class Meta:
        model = models.Assign
        fields = '__all__'
        # fields = ['id', 'patients', 'patients_id', 'categories_info', 'categories_info_id']


class PatientProfileSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), source='patient', write_only=True)

    categories_info = CategoriesInfoSerializer(read_only=True)
    categories_info_id = serializers.PrimaryKeyRelatedField(
        queryset=models.CategoriesInfo.objects.all(), source='categories_info', write_only=True)

    class Meta:
        model = models.Assign
        fields = '__all__'
