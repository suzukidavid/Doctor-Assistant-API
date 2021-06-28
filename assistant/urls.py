from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PatientViewSet,
    DiseaseLibraryViewSet,
    InvestigationViewSet,
    DiagnosisViewSet,
    SurgeryViewSet,
    FollowUpViewSet,
    InvestigationImageViewSet,
    InvestigationVideoViewSet,
    InvestigationDocumentViewSet,
    SurgeryImageViewSet,
    SurgeryVideoViewSet,
    SurgeryDocumentViewSet,

    # PatientProfile
)

router = DefaultRouter()
router.register('patients', PatientViewSet)  # for patient - post and get
router.register('disease_library', DiseaseLibraryViewSet)  # for patient - post and get
# router.register('patient/profile', PatientProfile)  # for patients profile - Search,
router.register('investigation', InvestigationViewSet)
router.register('diagnosis', DiagnosisViewSet)
router.register('surgery', SurgeryViewSet)
router.register('followup', FollowUpViewSet)

router.register('investigation/image', InvestigationImageViewSet)
router.register('investigation/video', InvestigationVideoViewSet)
router.register('investigation/document', InvestigationDocumentViewSet)

router.register('surgery/image', SurgeryImageViewSet)
router.register('surgery/video', SurgeryVideoViewSet)
router.register('surgery/document', SurgeryDocumentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
