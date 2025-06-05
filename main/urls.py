from django.urls import path
from .views import home, courses  # ✅ Added `courses` import

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),  # Courses route

]
