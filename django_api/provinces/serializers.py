from rest_framework import serializers
from provinces.models import Provinces


class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = ['id', 'province_name', 'gender', 'year', 'inhabitants']