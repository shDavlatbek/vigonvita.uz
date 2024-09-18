from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import News, Medicine


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {'news': News.objects.all()})
    
    
class NewsDetail(View):
    def get(self, request, slug):
        return render(request, 'coming-soon.html', {'news': News.objects.get(slug=slug)})
    

class ComingSoon(View):
    def get(self, request):
        return render(request, 'coming-soon.html')