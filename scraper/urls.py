# scraper app urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/scraper/submit/', views.SubmitLinkView.as_view(), name='submit-link'),
]