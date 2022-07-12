from rest_framework import serializers

from apps.courses.models import Course


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description', 'start_date', 'end_date')