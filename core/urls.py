from django.urls import path

from .views import index, game_updates_page, community

urlpatterns = [
    path("", index),
    path("updates", game_updates_page, name="updates"),
    path("community", community, name="community")
]
