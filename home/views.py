from django.shortcuts import render
from . models import Product, SecOne, Video, News

# Create your views here.
def index(request):
        products = Product.objects.all()
        secone = SecOne.objects.all()
        videos = Video.objects.all()
        news = News.objects.all()
        return render(request, 'home/index.html', {'products': products, 'secone': secone, 'videos': videos, 'news': news})

def about(request):
    return render(request, 'home/about.html')
