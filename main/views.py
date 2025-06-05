from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Backend is working!"})

def courses(request):
    return redirect(reverse('courses'))
