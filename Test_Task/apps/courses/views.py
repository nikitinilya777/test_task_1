from datetime import timedelta

from django.utils import timezone
from post_office import mail
from rest_framework import generics, views
from rest_framework.response import Response

from apps.courses.permissions import IsAdminOrReadOnly, IsReadOnlyRegular
from .models import Course, CourseMember
from .serializers import CoursesSerializer
from ..accounts.models import User


class CourseAPISortList(views.APIView):
    def get(self, request, *args, **kwargs):
        if kwargs.get("sort", None) is not None:
            if kwargs['sort'] == 'start_date' or kwargs['sort'] == 'description' or kwargs['sort'] == 'name':
                queryset = Course.objects.order_by(kwargs['sort'])
                serializer = CoursesSerializer(queryset, many=True)
                return Response(serializer.data)

        return Response({'Ошибка': 'Невозможно отсортировать!'})


class CourseAPIList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CourseAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CourseAPIRegular(generics.ListAPIView):
    serializer_class = CoursesSerializer
    permission_classes = (IsReadOnlyRegular,)

    def get_queryset(self):
        courses = []
        for courses_member in CourseMember.objects.filter(user=self.request.user):
            courses += [Course.objects.get(name=courses_member.course)]
        return courses

