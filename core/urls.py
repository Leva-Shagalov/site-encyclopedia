from django.urls import path

from .views import index, game_updates_page, community, page_article, add_article

urlpatterns = [
    path("", index),
    path("updates", game_updates_page, name="updates"),
    path("community", community, name="community"),
    path("article/<int:article_id>", page_article, name="article"),
    path("add_article", add_article, name="add_article")
]
