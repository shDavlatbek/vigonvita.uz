from django.contrib import admin
from django.urls import include, path
from .views import HomeView, NewsDetail, ComingSoon

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/<slug:slug>/', NewsDetail.as_view(), name="news_detail"),
    path("coming-soon/", ComingSoon.as_view(), name="coming-soon")
]
