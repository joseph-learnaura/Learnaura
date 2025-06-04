from django.urls import path
from .views import test_view

urlpatterns = [
    path('', test_view, name='home'),
    path('courses/', courses, name='courses'),  # Courses route

]
