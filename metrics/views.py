from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import ScopedRateThrottle
from .models import Metric
from .serializers import MetricSerializer, ContactSerializer

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


class ContactView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "contact"

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        subject = "Yangi murojaat: mahoratmarkaz.uz"
        body = (
            f"Ism familiya: {data['full_name']}\n"
            f"Telefon raqam: {data['phone']}\n"
            f"Xabar:\n{data['message']}"
        )

        email = EmailMessage(subject=subject, body=body, from_email=settings.DEFAULT_FROM_EMAIL, to=getattr(settings, "CONTACT_RECIPIENTS",[]))
        email.send(fail_silently=False)

        return Response({"message":"Murojaat yuborildi."}, status=status.HTTP_201_CREATED)