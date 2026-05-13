from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import News


def news_list(request):
    news_list = News.objects.filter(published=True)
    # get recently viewed objects from session
    recent_items = _get_recent_objects(request)
    return render(request, 'news/news_list.html', {'news_list': news_list, 'recent_items': recent_items})


def news_detail(request, slug):
    item = get_object_or_404(News, slug=slug, published=True)
    # Track recently viewed news in session (store slugs)
    recent = request.session.get('recent_news', [])
    # remove if already present
    if item.slug in recent:
        recent.remove(item.slug)
    recent.insert(0, item.slug)
    # keep only last 10
    recent = recent[:10]
    request.session['recent_news'] = recent
    request.session.modified = True

    return render(request, 'news/news_detail.html', {'news': item})


def news_feed_json(request):
    """Devuelve un feed JSON con las últimas noticias publicadas."""
    items = News.objects.filter(published=True).order_by('-created_at')[:20]
    data = []
    for it in items:
        image_url = None
        try:
            if it.image:
                image_url = request.build_absolute_uri(it.image.url)
        except Exception:
            image_url = None

        author = None
        if it.author:
            author = getattr(it.author, 'get_full_name', None)
            if callable(author):
                author = it.author.get_full_name() or it.author.username
            else:
                author = getattr(it.author, 'username', None)

        data.append({
            'title': it.title,
            'slug': it.slug,
            'excerpt': it.excerpt,
            'image': image_url,
            'author': author,
            'created_at': it.created_at.isoformat(),
            'url': request.build_absolute_uri(it.get_absolute_url() if hasattr(it, 'get_absolute_url') else f"/noticias/{it.slug}/"),
        })

    return JsonResponse({'news': data}, json_dumps_params={'ensure_ascii': False})


def _get_recent_objects(request):
    """Helper to return News queryset ordered as in session recent list."""
    recent = request.session.get('recent_news', [])
    if not recent:
        return News.objects.none()
    preserved = {slug: i for i, slug in enumerate(recent)}
    objs = list(News.objects.filter(slug__in=recent))
    # sort by session order
    objs.sort(key=lambda o: preserved.get(o.slug, 999))
    return objs
