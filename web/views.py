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
    def get(self, request):
        return render(request, os.path.join(PAGES_DIR, "news.html"), {'news': News.objects.all()})
    
    
class NewsDetail(View):
    def get(self, request, slug):
        news_obj = News.objects.get(slug=slug)
        news_obj.views += 1
        news_obj.save()
        return render(request, os.path.join(PAGES_DIR, "news-detail.html"), {'news': news_obj, 'latest_news': News.objects.order_by('-created_at')[:2]})


class ComingSoon(View):
    def get(self, request):
        return render(request, 'coming-soon.html')