from django.urls import path
from .views import credentialsTemplateView
urlpatterns = [
    path('templates/', credentialsTemplateView.as_view(), name='credentials-template'),
]