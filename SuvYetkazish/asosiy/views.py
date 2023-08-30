from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
# Create your views here.

class SuvlarAPIView(APIView):
    def get(self, request):
        suvlar = Suv.objects.all()
        serializer = SuvSerializer(suvlar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class SuvAPIView(APIView):
    def get(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)

    def put(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        suv = Suv.objects.get(id=pk).delete()
        d = {
            "xabar":"Suv o'chirildi!"
        }
        return Response(d,status=status.HTTP_200_OK)

class MijozlarAPIView(APIView):
    def get(self, request):
        mijozlar = Mijoz.objects.all()
        serializer = MijozSerializer(mijozlar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MijozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class MijozAPIView(APIView):
    def get(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)

    def put(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk).delete()
        d = {
            "xabar":"Mijoz o'chirildi!"
        }
        return Response(d,status=status.HTTP_200_OK)

class BuyurtmalarAPIView(APIView):
    def get(self, request):
        buyurtmalar = Buyurtma.objects.all()
        serializer =BuyurtmaSerializer(buyurtmalar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class AdminlarAPIView(APIView):
    def get(self, request):
        adminlar = Admin.objects.all()
        serializer =AdminSerializer(adminlar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class AdminAPIView(APIView):
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

class HaydovchilarAPIView(APIView):
    def get(self, request):
        haydovchilar = Haydovchi.objects.all()
        serializer =HaydovchiSerializer(haydovchilar,many=True)
        return Response(serializer.data)

class HaydovchiAPIView(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)

