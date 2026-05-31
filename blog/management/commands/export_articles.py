import json
import sys

from django.core.management.base import BaseCommand

from blog.models import Article


class Command(BaseCommand):
    help = 'Export all articles to JSON with embedded related objects'

    def add_arguments(self, parser):
        parser.add_argument('--output', type=str, help='Write JSON to this file instead of stdout')

    def handle(self, *args, **options):
        articles = Article.objects.select_related('topic', 'series').prefetch_related('tags').order_by('created_at')

        data = []
        for article in articles:
            topic = article.topic
            series = article.series

            data.append({
                'title': article.title,
                'slug': article.slug,
                'content': article.content,
                'is_published': article.is_published,
                'view_count': article.view_count,
                'created_at': article.created_at.isoformat(),
                'category': {
                    'name': topic.name,
                    'slug': topic.slug,
                    'description': topic.description,
                } if topic else None,
                'tags': [
                    {'name': tag.name, 'slug': tag.slug}
                    for tag in article.tags.all()
                ],
                'series': {
                    'title': series.title,
                    'slug': series.slug,
                    'description': series.description,
                    'sequence_number': article.series_sequence_number,
                } if series else None,
            })

        output = json.dumps(data, indent=2, ensure_ascii=False)

        output_path = options.get('output')
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
            self.stdout.write(self.style.SUCCESS(f'Exported {len(data)} articles to {output_path}'))
        else:
            sys.stdout.write(output)
            sys.stdout.write('\n')