from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentListView(APIView):
    def get(self, request):
        # students = Student.objects.all()
        # # Perform any necessary serialization or data transformation
        # # return Response(...)
        # serialized_students = serializers.serialize('json', students)
        # return JsonResponse(serialized_students, safe=False)
        # # return Response(students)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
@login_required
def profile(request):
    return render(request, 'profile.html')