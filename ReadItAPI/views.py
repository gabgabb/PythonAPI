from .models import Communaute
from .serializers import CommunauteSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render,HttpResponseRedirect,Http404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def CommunauteView(request):

    if request.method == 'GET':
        items = Communaute.objects.all()
        serializer = CommunauteSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommunauteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
