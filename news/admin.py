from django.contrib import admin
from .models import Article
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)
@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'body')

