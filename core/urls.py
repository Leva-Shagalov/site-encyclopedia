from django.urls import path

from .views import index, game_updates_page

urlpatterns = [
    path("", index),
    path("updates", game_updates_page, name="updates")
]
