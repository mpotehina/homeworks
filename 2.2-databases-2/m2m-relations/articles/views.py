from django.shortcuts import render
from django.db.models import Prefetch
from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.prefetch_related('scopes').all()

    for article in articles:
        print(article.tag)

    context = {
        'object_list': articles
    }

    return render(request, template, context)
