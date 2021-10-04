from django.urls import path
from news_app import views

urlpatterns = [
    path('', views.main, name='index'),
    path('about', views.about, name='about'),
    path('videos', views.videos, name='videos'),
    path('ipo', views.beautifulsoup, name='news'),
]
