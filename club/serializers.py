from rest_framework import serializers
from .models import *


class ClubCreateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=250, required=True)
    description = serializers.CharField()

    class Meta:
        model = Club
        fields = ('name', 'description')

    def create(self, validated_data):
        return Club.objects.create(**validated_data)
