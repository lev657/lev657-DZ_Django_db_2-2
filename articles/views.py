from django.shortcuts import render

from .models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {'articles': Article.objects.order_by(ordering).all()}
    print(context)
    return render(request, template, context)
