from rest_framework import viewsets, permissions
from account.permissions import IsDoctor
from . import serializers
from . import models
from rest_framework.response import Response


class PatientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Patient class"""

    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class CategoriesInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the CategoriesInfo class"""

    queryset = models.CategoriesInfo.objects.all()
    serializer_class = serializers.CategoriesInfoSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class MediaImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the MediaImage class"""

    queryset = models.MediaImage.objects.all()
    serializer_class = serializers.MediaImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class MediaVideoViewSet(viewsets.ModelViewSet):
    """ViewSet for the MediaVideo class"""

    queryset = models.MediaVideo.objects.all()
    serializer_class = serializers.MediaVideoSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class MediaDocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for the MediaDocument class"""

    queryset = models.MediaDocument.objects.all()
    serializer_class = serializers.MediaDocumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]


class AssignViewSet(viewsets.ModelViewSet):
    """ViewSet for the Assign class"""

    queryset = models.Assign.objects.all()
    serializer_class = serializers.AssignSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]



class PatientProfile(viewsets.ModelViewSet):
    """
    ViewSet for the Patient Profile where
        --> ALl Media and assign info will show
    """
    queryset = models.Assign.objects.all()
    serializer_class = serializers.PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_queryset(self, media_image=False, *args, **kwargs):

        if self.request.user.doctors:
            queryset = self.queryset.filter(patient_id__assign_doctor=self.request.user.doctors)

            if media_image:
                #image_queryset = models.MediaImage.objects.filter(assign__patient__assign_doctor=)
                pass
        else:
            queryset = None

        return queryset

    def list(self, request, *args, **kwargs):
        media_image = self.get_queryset(media_image=True)
        total_due = self.get_queryset()

        patient_profile_data = {
            'count': self.get_queryset().count(),
            'full_info': serializers.PatientProfileSerializer(self.get_queryset(), many=True).data

        }
        return Response(patient_profile_data)
