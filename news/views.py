from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.order_by("-created_at")
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"
    search_fields = ["title", "body"]
    ordering_fields = ["created_at", "title"]

