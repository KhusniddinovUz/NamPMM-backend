from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import RetrieveAPIView
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

    # def get_queryset(self):
    #     qs = Article.objects.order_by("-created_at")
    #     # convert queryset to list, then repeat it 3 times
    #     return list(qs) * 3

class HomepageArticlesViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    ordering_fields = ["created_at", "title"]

    def get_queryset(self):
        main_news = Article.objects.filter(main_news=True).order_by("-created_at").first()
        small_news = Article.objects.filter(main_news=False).order_by("-created_at")[:4]
        articles = []

        if main_news:
            articles.append(main_news)
        articles.extend(small_news)
        return articles

class SingleArticleViewSet(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
