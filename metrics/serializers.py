from rest_framework import serializers
from .models import Metric

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ["view_count", "like_count"]

class ContactSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=24)
    message = serializers.CharField(max_length=3000)