from django import forms

from blog.models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'series', 'series_sequence_number', 'content', 'topic', 'tags', 'image')
