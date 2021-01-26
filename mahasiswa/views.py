from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Mahasiswa
from .serializers import MahasiswaSerializer


def api_create_and_view(request):
    if request.method == 'GET':
        mahasiswa = Mahasiswa.objects.all()
        mahasiswa_serializer = MahasiswaSerializer(mahasiswa, many=True)
        return JsonResponse(mahasiswa_serializer.data, safe=False)

    elif request.method == 'POST':
        data_mahasiswa = JSONParser().parse(request)
        mahasiswa_serializer = MahasiswaSerializer(data=data_mahasiswa)
        if mahasiswa_serializer.is_valid():
            mahasiswa_serializer.save()
            return JsonResponse(mahasiswa_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(mahasiswa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def api_viewbyid_update_delete(request, pk):
    try:
        mahasiswa = Mahasiswa.objects.get(pk=pk)
    except Mahasiswa.DoesNotExist:
        return HttpResponse("Tidak menemukan ID/Method")

    if request.method == 'GET':
        mahasiswa_serializer = MahasiswaSerializer(mahasiswa)
        return JsonResponse(mahasiswa_serializer.data)

    elif request.method == 'PUT':
        mahasiswa_data = JSONParser().parse(request)
        mahasiswa_serializer = MahasiswaSerializer(
            mahasiswa, data=mahasiswa_data)
        if mahasiswa_serializer.is_valid():
            mahasiswa_serializer.save()
            return JsonResponse(mahasiswa_serializer.data)
        return JsonResponse(mahasiswa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Mahasiswa.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
