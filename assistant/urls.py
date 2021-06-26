from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PatientViewSet,
    MediaImageViewSet,
    MediaVideoViewSet,
    MediaDocumentViewSet,
    AssignViewSet,
    # PatientProfile
)

router = DefaultRouter()
router.register('patients', PatientViewSet)  # for patient - post and get
# router.register('patient/profile', PatientProfile)  # for patients profile - Search,
router.register('assign', AssignViewSet)  # for patient Assign the Categories - post and get
router.register('image', MediaImageViewSet)  # for Categories Assign Image - post and get
router.register('video', MediaVideoViewSet)  # for Categories Assign Video - post and get
router.register('document', MediaDocumentViewSet)  # for Categories Assign document - post and get

urlpatterns = [
    path('api/', include(router.urls)),
]
