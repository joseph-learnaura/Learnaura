from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Backend is working!"})

def courses(request):
    return render(request, 'courses.html')  # ✅ Ensure `courses.html` exists