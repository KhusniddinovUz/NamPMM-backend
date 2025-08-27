from django.urls import path
from .views import IncrementSiteViewCount, IncrementSiteLikeCount, ContactView

urlpatterns = [
    path("increment-view-count/", IncrementSiteViewCount.as_view(), name="increment-view-count"),
    path("increment-like-count/", IncrementSiteLikeCount.as_view(), name="increment-like-count"),
    path("contact/", ContactView.as_view(), name="contact")
]