from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Metric
from .serializers import MetricSerializer

def get_metrics():
    metrics, _ = Metric.objects.get_or_create(pk=1)
    return metrics

class IncrementSiteViewCount(APIView):
    def post(self, request):
        metrics = get_metrics()
        Metric.objects.filter(pk=metrics.pk).update(view_count=metrics.view_count + 1)
        metrics.refresh_from_db(fields=["view_count"])
        serializer = MetricSerializer(metrics)
        return Response(serializer.data)


class IncrementSiteLikeCount(APIView):
    def post(self, request):
        metrics = get_metrics()
        Metric.objects.filter(pk=metrics.pk).update(like_count=metrics.like_count + 1)
        metrics.refresh_from_db(fields=["like_count"])
        serializer = MetricSerializer(metrics)
        return Response(serializer.data)