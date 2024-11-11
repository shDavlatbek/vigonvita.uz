from django.contrib import admin
from django.urls import include, path
from .views import HomeView, NewsAll, NewsDetail, MedicineDetail, ComingSoon

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsAll.as_view(), name="news-all"),
    path('news/<slug:slug>/', NewsDetail.as_view(), name="news-detail"),
    path('medicine/<int:pk>/', MedicineDetail.as_view(), name="medicine-detail"),
    path("coming-soon/", ComingSoon.as_view(), name="coming-soon")
]
