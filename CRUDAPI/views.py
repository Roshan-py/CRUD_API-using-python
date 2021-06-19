from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


# Create your views here.
@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
def crud_api(request,pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None:
            pst=Post.objects.get(id= id)
            serializer=PostSerializer(pst)
            return Response(serializer.data)
        pst=Post.objects.all()
        serializer=PostSerializer(pst, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)


    if request.method == 'PUT':
        id = pk
        pst=Post.objects.get(pk=id)
        serializer=PostSerializer(pst, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
       id = pk
       pst=Post.objects.get(pk=id)
       pst.delete()
       return Response({'msg':'data deleted'})
