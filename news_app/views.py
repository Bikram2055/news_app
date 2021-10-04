from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import News, Videos
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests


def main(request):
    query = News.objects.all()
    paginator = Paginator(query, 5)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'index.html', {'data': data})


def about(request):
    return render(request, 'about.html')


def beautifulsoup(request):
    return redirect('https://iporesult.cdsc.com.np/?fbclid=IwAR1ClBdhtKR1FSMtpfebv1iNYn4KUqc4fG4bn1FFLOKPe5yr9lDTAhITs6s')


def videos(request):
    videos = Videos.objects.all()
    video = Videos.objects.filter(id=1)
    return render(request, 'videos.html', {'videos': videos, 'video': video})
