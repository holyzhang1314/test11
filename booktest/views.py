from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo,HeroInfo

# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    bookes = HeroInfo.objects.all()
    return render(request,'booktest/index.html',{'dicts':books,'dictes':bookes})




def indexone(request):
    return HttpResponse('誓约胜利之剑')
