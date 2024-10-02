from django.urls import path
from news.views import news, post, forum


urlpatterns = [
    path('news/', news),
    path('post/', post),
    path('forum/', forum),
]
