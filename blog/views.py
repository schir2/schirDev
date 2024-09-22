from django.shortcuts import render

from blog.models import Article


def home_view(request):
    context = {}
    template_name = ''
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
