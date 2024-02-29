from provinces.models import Provinces
from provinces.serializers import ProvincesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProvincesList(APIView):
    """
    List all provinces, or create a new snippet.
    """
    def get(self, request, format=None):
        provinces = Provinces.objects.all()
        serializer = ProvincesSerializer(provinces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProvincesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProvincesDetail(APIView):
    """
    Retrieve, update or delete a province instance.
    """
    def get_object(self, pk):
        try:
            return Provinces.objects.get(pk=pk)
        except Provinces.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        province = self.get_object(pk)
        serializer = ProvincesSerializer(province)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        province = self.get_object(pk)
        serializer = ProvincesSerializer(province, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        province = self.get_object(pk)
        province.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)