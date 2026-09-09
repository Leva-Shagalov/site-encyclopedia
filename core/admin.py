from django.contrib import admin

from .models import ArticleTopic, Article, ArticleContent

admin.site.register(ArticleTopic)
admin.site.register(Article)
admin.site.register(ArticleContent)
