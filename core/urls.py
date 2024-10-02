from django.urls import path
from core.views import index, about, contact


urlpatterns = [
    path('', index, name='home'),
    path('about/', about),
    path('contact/', contact),
]
