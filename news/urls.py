from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, HomepageArticlesViewSet, SingleArticleViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet, basename="article")
router.register(r"homepage-news", HomepageArticlesViewSet, basename="main-news")

urlpatterns = [
    path("", include(router.urls)),
    path("news/<slug:slug>/", SingleArticleViewSet.as_view(), name="single-article")
]
