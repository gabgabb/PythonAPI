from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CommunauteModel
from .serializers import CommunauteSerializers
import unittest

def helloWorld():
    print("badar")

@csrf_exempt
def CommunautesView(request):
    if request.method == 'GET':
        communaute = CommunauteModel.objects.all()
        serializer = CommunauteSerializers(communaute, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommunauteSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def CommunauteView(request, nb):
    try:
        communaute = CommunauteModel.objects.get(id=nb)
    except CommunauteModel.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = CommunauteSerializers(communaute)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommunauteSerializers(communaute, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        communaute.delete()
        return HttpResponse(status=204)




