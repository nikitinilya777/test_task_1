from django.contrib import admin
from django.urls import path, include

from apps.courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('courses/', CourseAPIList.as_view()),
    path('courses/sort/<str:sort>/', CourseAPISortList.as_view()),
    path('courses/<int:pk>/', CourseAPICRUD.as_view()),
    path('courses/mycourses/', CourseAPIRegular.as_view()),
    path('courses/mycourses/<int:pk>/', CourseAPIRegular.as_view()),
]
