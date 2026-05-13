from django.urls import path
from . import views
from . import feeds

app_name = 'news'

urlpatterns = [
    path('noticias/', views.news_list, name='news_list'),
    path('noticias/feed.json', views.news_feed_json, name='news_feed_json'),
    path('noticias/feed/', feeds.LatestNewsFeed(), name='news_feed_rss'),
    path('noticias/<slug:slug>/', views.news_detail, name='news_detail'),
]
