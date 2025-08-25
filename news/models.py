from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True, max_length=255)
    main_news = models.BooleanField(default=False, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']


    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "article"
            base = base[:20]  # limit base to 20 chars

            slug = base
            i = 1

            # ensure uniqueness
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                suffix = f"-{i}"
                slug = f"{base[:20 - len(suffix)]}{suffix}"
                i += 1

            self.slug = slug

        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
