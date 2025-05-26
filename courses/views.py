from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from courses.models import Course
from courses.serializers import CourseSerializer


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    def list(self, request, *args, **kwargs):


        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)