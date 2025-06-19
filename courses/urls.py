from django.urls import include, path
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/enroll/', EnrollmentViewSet.as_view())
]