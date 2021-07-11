from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from account.permissions import IsDoctor
from . import serializers
from . import models
from .filters import PatientFilter


class PatientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Patient class"""

    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ('name', 'phone', 'sex',)
    filter_class = PatientFilter


class DiseaseLibraryViewSet(viewsets.ModelViewSet):
    """
    ViewSet For Disease Library
    """
    queryset = models.DiseaseLibrary.objects.all()
    serializer_class = serializers.DiseaseLibrarySerializer
    permission_classes = [permissions.IsAuthenticated]


class FamilyHistoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet For Disease Family History
    """
    queryset = models.FamilyHistory.objects.all()
    serializer_class = serializers.FamilyHistorySerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

class HistoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet For Disease Family History
    """
    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class InvestigationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Investigation class"""

    queryset = models.Investigation.objects.all()
    serializer_class = serializers.InvestigationSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class SurgeryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Surgery class"""

    queryset = models.Surgery.objects.all()
    serializer_class = serializers.SurgerySerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class FollowUpViewSet(viewsets.ModelViewSet):
    """ViewSet for the FollowUp class"""

    queryset = models.FollowUp.objects.all()
    serializer_class = serializers.FollowUpSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class DiagnosisViewSet(viewsets.ModelViewSet):
    """ViewSet for the Diagnosis class"""

    queryset = models.Diagnosis.objects.all()
    serializer_class = serializers.DiagnosisSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


"""
Media ViewSets 
"""


class InvestigationImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the InvestigationImage class"""

    queryset = models.InvestigationImage.objects.all()
    serializer_class = serializers.InvestigationImageSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class InvestigationVideoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Investigation Video class"""

    queryset = models.InvestigationVideo.objects.all()
    serializer_class = serializers.InvestigationVideoSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class InvestigationDocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Investigation Document class"""

    queryset = models.InvestigationDocument.objects.all()
    serializer_class = serializers.InvestigationDocumentSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class SurgeryImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the SurgeryImage class"""

    queryset = models.SurgeryImage.objects.all()
    serializer_class = serializers.SurgeryImageSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class SurgeryVideoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Surgery Video class"""

    queryset = models.SurgeryVideo.objects.all()
    serializer_class = serializers.SurgeryVideoSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class SurgeryDocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Surgery Document class"""

    queryset = models.SurgeryDocument.objects.all()
    serializer_class = serializers.SurgeryDocumentSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class FollowUpImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the SurgeryImage class"""

    queryset = models.FollowUpImage.objects.all()
    serializer_class = serializers.FollowUpImageSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class FollowUpVideoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Surgery Video class"""

    queryset = models.FollowUpVideo.objects.all()
    serializer_class = serializers.FollowUpVideoSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class FollowUpDocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Surgery Document class"""

    queryset = models.FollowUpDocument.objects.all()
    serializer_class = serializers.FollowUpDocumentSerializer

    permission_classes = [permissions.IsAuthenticated, IsDoctor]

#
# class PatientProfile(viewsets.ModelViewSet):
#     """
#     ViewSet for the Patient Profile where
#         --> ALl Media and assign info will show
#     """
#     queryset = models.Patient.objects.all()
#     assign_queryset = models.Assign.objects.all()
#     serializer_class = serializers.PatientProfileSerializer
#     permission_classes = [permissions.IsAuthenticated, IsDoctor]
#
#     def get_queryset(self, media_image=False, media_document=False, media_video=False, patient=False, *args, **kwargs):
#
#         if self.request.user.doctors:
#             queryset = self.queryset.filter(assign_doctor=self.request.user.doctors)
#
#             # To get all assign categories information for specific patient
#             if patient:
#                 return self.assign_queryset.filter(patient_id=patient)
#
#             if media_image:
#                 return models.MediaImage.objects.filter(assign=media_image)
#
#             elif media_video:
#                 return models.MediaVideo.objects.filter(assign=media_video)
#
#             elif media_document:
#                 return models.MediaDocument.objects.filter(assign=media_document)
#
#         else:
#             queryset = None
#
#         return queryset
#
#     def list(self, request, *args, **kwargs):
#         # media_image = self.get_queryset(media_image=True)
#         patients_info = self.get_queryset()
#
#         all_patient_profile_data = {}  # to add all patient info
#
#         for info in patients_info:
#
#             # Modify Assign to get categories with media
#             assign_info = self.get_queryset(patient=info.id)
#             all_assign_main = {}
#
#             # Get Data from Assign Model
#             assign_count = 1
#             for assign in assign_info:
#
#                 media_images = {}
#                 media_images_count = 1
#                 media_image = self.get_queryset(media_image=assign.id)
#                 for image in media_image:
#                     media_images[media_images_count] = str(image.image),
#                     media_images_count += 1
#
#                 media_videos = {}
#                 media_videos_count = 1
#                 media_video = self.get_queryset(media_video=assign.id)
#                 for video in media_video:
#                     media_videos[media_videos_count] = str(video.video),
#                     media_videos_count += 1
#
#                 media_documents = {}
#                 media_documents_count = 1
#                 media_document = self.get_queryset(media_document=assign.id)
#                 for document in media_document:
#                     media_documents[media_documents_count] = str(document.document),
#                     media_documents_count += 1
#
#                 categories_info = {
#                                       'type': assign.categories_info.type,
#                                       'type_name': assign.categories_info.type_name
#                                   },
#
#                 assign_main = {
#                     'categories_info': categories_info,
#                     'specimen': assign.specimen,
#                     'investigation': assign.investigation,
#                     'referred_by': assign.referred_by,
#                     'created_date': assign.created_date,
#                     'finishing_date': assign.finishing_date,
#                     'images': media_images,
#                     'videos': media_videos,
#                     'documents': media_documents,
#                 }
#                 all_assign_main[assign_count] = assign_main
#                 assign_count += 1
#
#             patient_profile_data = {
#                 'diagnosis': info.diagnosis,
#                 'sex': info.sex,
#                 'age': info.age,
#                 'phone': info.phone,
#                 'address': info.address,
#                 'prof_surgeon_consultant': info.prof_surgeon_consultant,
#                 'date_of_discharge': info.date_of_discharge,
#                 'date_of_admission': info.date_of_admission,
#
#                 'assign_info': all_assign_main
#
#             }
#             all_patient_profile_data[info.name] = patient_profile_data
#
#         return Response(all_patient_profile_data)
