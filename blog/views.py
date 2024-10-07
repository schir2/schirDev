from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST, require_GET
from django_cotton.cotton_loader import CottonCompiler

from blog.forms import ArticleForm
from blog.models import Article, Topic, FeaturedArticle, Tag, ArticleInteraction


def css_display_cheatsheet_view(request):
    template_name = 'blog/resources/css_display_cheatsheet.html'
    context = dict()
    return render(request, template_name=template_name, context=context)


def home_view(request):
    context = {}
    template_name = 'blog/home.html'
    latest_articles = Article.objects.order_by('-created_at')[:3]
    popular_articles = Article.objects.order_by('-popularity_score')[:10]
    featured_articles = FeaturedArticle.objects.order_by('-created_at')[:2]
    tags = Tag.objects.all()
    topics = Topic.objects.all()
    context['popular_articles'] = popular_articles
    context['latest_articles'] = latest_articles
    context['featured_articles'] = featured_articles
    context['topics'] = topics
    context['tags'] = tags
    return render(request, template_name=template_name, context=context)


def article_list_view(request):
    template_name = 'blog/article_list.html'
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    return render(request, template_name=template_name, context=context)


def article_detail_view(request, slug):
    template_name = 'blog/article_detail.html'
    context = {}

    article = get_object_or_404(
        Article.objects.select_related('creator', 'topic').prefetch_related('tags', 'interactions'),
        slug=slug
    )

    article.increment_view_count(request)

    cotton_compiler = CottonCompiler()
    processed_content = cotton_compiler.process(article.content, template_name)

    # Render the content using Django's Template class
    rendered_content = Template(processed_content).render(Context({}))

    context["article"] = article
    context["content"] = rendered_content
    context["user_has_liked"] = article.user_has_liked(request.user)
    context["user_has_disliked"] = article.user_has_disliked(request.user)

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


def article_archive_view(request, slug: str):
    return


def article_edit_view(request, slug: str):
    return


def article_delete_view(request, slug: str):
    return


@require_GET
def article_view_count_view(request, slug: str):
    article = get_object_or_404(Article, slug=slug)
    return HttpResponse(article.view_count, content_type='text/html')


@require_GET
def article_comments_view(request, slug):
    """
    Fetch and render comments for a specific article.

    This view is designed to be called via HTMX for lazy loading of comments.
    It renders a partial template with the comments for the specified article.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the article to fetch comments for.

    Returns:
        HttpResponse: Rendered HTML of the comments.
    """
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all().select_related('creator').order_by('-created_at')

    context = {
        'article': article,
        'comments': comments,
    }

    html_content = render_to_string('blog/partials/comments_list.html', context, request=request)
    return HttpResponse(html_content)


def article_add_comment_view(request):
    return


def tag_list_view(request):
    template_name = 'blog/tag_list.html'
    context = {}
    tags = Tag.objects.all()
    context['tags'] = tags
    return render(request, template_name=template_name, context=context)


def tag_detail_view(request, slug: str):
    template_name = 'blog/tag_detail.html'
    context = {}
    tag = get_object_or_404(Tag, slug=slug)
    context['tag'] = tag
    return render(request, template_name=template_name, context=context)


def tag_create_view(request):
    template_name = 'blog/tag_create.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def tag_edit_view(request):
    template_name = 'blog/tag_edit.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def tag_delete_view(request):
    template_name = 'blog/tag_delete.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def topic_list_view(request):
    template_name = 'blog/topic_list.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def topic_detail_view(request, slug: str):
    template_name = 'blog/topic_detail.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def topic_create_view(request):
    template_name = 'blog/topic_create.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def topic_edit_view(request):
    template_name = 'blog/topic_edit.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def topic_delete_view(request):
    template_name = 'blog/topic_delete.html'
    context = {}
    return render(request, template_name=template_name, context=context)


def article_like_count_view(request, slug):
    article = Article.objects.get(slug=slug)
    like_count = article.interactions.filter(interaction_type='like').count()
    return HttpResponse(f"{like_count} likes")


def article_dislike_count_view(request, slug):
    article = Article.objects.get(slug=slug)
    like_count = article.interactions.filter(interaction_type='dislike').count()
    return HttpResponse(f"{like_count} dislikes")


@require_POST
def toggle_like_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    interaction, created = ArticleInteraction.objects.get_or_create(
        article=article,
        creator=request.user,
        defaults={'interaction_type': 'like'}
    )

    if not created and interaction.interaction_type == 'like':
        interaction.delete()
        liked = False
    else:
        interaction.interaction_type = 'like'
        interaction.save()
        liked = True

    like_count = article.interactions.filter(interaction_type='like').count()
    dislike_count = article.interactions.filter(interaction_type='dislike').count()

    context = {
        'article': article,
        'like_count': like_count,
        'dislike_count': dislike_count,
        'liked': liked,
        'disliked': False,
    }

    response = HttpResponse(render_to_string('blog/partials/like_dislike_buttons.html', context))
    response['HX-Trigger'] = 'interactionUpdated'
    return response


@require_POST
def toggle_dislike_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    interaction, created = ArticleInteraction.objects.get_or_create(
        article=article,
        creator=request.user,
        defaults={'interaction_type': 'dislike'}
    )

    if not created and interaction.interaction_type == 'dislike':
        interaction.delete()
        disliked = False
    else:
        interaction.interaction_type = 'dislike'
        interaction.save()
        disliked = True

    like_count = article.interactions.filter(interaction_type='like').count()
    dislike_count = article.interactions.filter(interaction_type='dislike').count()

    context = {
        'article': article,
        'like_count': like_count,
        'dislike_count': dislike_count,
        'liked': False,
        'disliked': disliked,
    }

    response = HttpResponse(render_to_string('blog/partials/like_dislike_buttons.html', context))
    response['HX-Trigger'] = 'interactionUpdated'
    return response
