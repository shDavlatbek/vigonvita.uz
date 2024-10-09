import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import News, Medicine

PAGES_DIR = "pages"


class HomeView(View):
    def get(self, request):
        return render(request,  os.path.join(PAGES_DIR, "home.html"), {'news': News.objects.all()})
    
    
class NewsAll(View):
    def get(self, request, slug):
        return render(request, os.path.join(PAGES_DIR, "news.html"), {'news': News.objects.all()})
    
    
class NewsDetail(View):
    def get(self, request, slug):
        return render(request, os.path.join(PAGES_DIR, "news-detail.html"), {'news': News.objects.get(slug=slug)})


class ComingSoon(View):
    def get(self, request):
        return render(request, 'coming-soon.html')