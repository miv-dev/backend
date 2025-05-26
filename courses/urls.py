from django.urls import include, path
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet

router = DefaultRouter()
router.register(r'', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]