from django.urls import path
# from django.conf.urls import url
from . import views
from database.views import *


urlpatterns = [
    path('', ReactView.as_view(), name="anything"),
    path('translators/', views.translators),
    path('clients/', views.clients),
    path('venues/', views.venues),
]