from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, HomepageArticlesViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet, basename="article")
router.register(r"homepage-news", HomepageArticlesViewSet, basename="main-news")

urlpatterns = [path("", include(router.urls))]
