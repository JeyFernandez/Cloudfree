from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import News


class LatestNewsFeed(Feed):
    title = "CloudFree - Últimas Noticias"
    link = "/noticias/"
    description = "Las últimas noticias y novedades de CloudFree."

    def items(self):
        return News.objects.filter(published=True).order_by('-created_at')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt or item.content[:200]

    def item_link(self, item):
        return reverse('news:news_detail', args=[item.slug])

    def item_pubdate(self, item):
        return item.created_at

    def item_author_name(self, item):
        if item.author:
            return getattr(item.author, 'get_full_name', None)() or item.author.username
        return None
