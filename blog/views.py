from django.shortcuts import render

from blog.models import Article


def blog_index_view(request):
    context = {}
    template_name = 'blog/index.html'
    articles = Article.objects.all()
    context['articles'] = articles
    return render(request, template_name=template_name, context=context)


def article_list_view(request):
    template_name = 'blog/article_list.html'
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    return render(request, template_name=template_name, context=context)


def article_detail_view(request, slug):
    template_name = 'blog/article.html'
    context = {}
    article = Article.objects.get(slug=slug)
    context["article"] = article
    return render(request, template_name=template_name, context=context)
