from django.core.management.base import BaseCommand

from blog.utils.mock_data import generate_mock_blog_data


class Command(BaseCommand):
    help = 'Generates mock data for the blog'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=100, help='Number of users to create')
        parser.add_argument('--articles', type=int, default=200, help='Number of articles to create')
        parser.add_argument('--topics', type=int, default=10, help='Number of topics to create')
        parser.add_argument('--tags', type=int, default=30, help='Number of tags to create')

    def handle(self, *args, **options):
        generate_mock_blog_data(
            num_users=options['users'],
            num_articles=options['articles'],
            num_topics=options['topics'],
            num_tags=options['tags']
        )
        self.stdout.write(self.style.SUCCESS('Successfully generated mock data'))