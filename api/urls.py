from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import include, path

from people.api_views import (
    CurrentUserView, GroupViewSet, ImageViewSet, UserViewSet
    # EmployeeViewSet, FileUploadViewSet,
    # PerformanceReviewViewSet, ReviewNoteViewSet, SignatureViewSet, 
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('v1/current-user/', CurrentUserView.as_view(), name='current_user'),
]

router = routers.DefaultRouter(trailing_slash=False)
router.register('v1/user', UserViewSet)
router.register('v1/groups', GroupViewSet)
router.register('v1/images', ImageViewSet)
# router.register('v1/stories', StoryViewSet)
# router.register('v1/employee', EmployeeViewSet)
# router.register('v1/performancereview', PerformanceReviewViewSet)
# router.register('v1/fileupload', FileUploadViewSet, basename='fileupload')
# router.register('v1/signature', SignatureViewSet)
# router.register('v1/reviewnote', ReviewNoteViewSet)

urlpatterns = router.urls + urlpatterns
