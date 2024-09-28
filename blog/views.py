from django.db import IntegrityError
from django.shortcuts import render, redirect

from blog.forms import ArticleForm
from blog.models import Article, Comment, Topic, FeaturedArticle


def blog_index_view(request):
    context = {}
    template_name = 'blog/index.html'
    latest_articles = Article.objects.order_by('-created_at')[:5]
    featured_articles = FeaturedArticle.objects.order_by('-created_at')[:5]
    topics = Topic.objects.all()
    context['latest_articles'] = latest_articles
    context['featured_articles'] = featured_articles
    context['topics'] = topics
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


def article_create_view(request):
    template_name = 'blog/article_create.html'
    context = {}
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            try:
                article = form.save()
                return redirect('blog:article_detail', slug=article.slug)
            except IntegrityError:
                form.add_error('title', "An article with this title already exists.")
    else:
        form = ArticleForm()
    context['form'] = form
    return render(request, template_name=template_name, context=context)
