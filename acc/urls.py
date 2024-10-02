from django.urls import path
from acc.views import login, registration, Featured


urlpatterns = [
    path('login/', login),
    path('registration/', registration),
    path('Featured/', Featured),
]
