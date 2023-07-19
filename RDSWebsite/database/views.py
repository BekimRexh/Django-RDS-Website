from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import * 
from rest_framework.response import Response
from .serializer import *


class ReactView(APIView):
    def get(self, request):
        output_data = [{"employee": output.employee,
                   "department": output.department}
                   for output in React.objects.all()]
        return Response(output_data)
        
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



def home(request):
    return render(request, 'database\dashboard.html')

def translators(request):
    return render(request, 'database\\translators.html')

def clients(request):
    return render(request, 'database\\clients.html')

def venues(request):
    return render(request, 'database\\venues.html')
