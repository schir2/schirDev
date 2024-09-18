from django.core.management import call_command, BaseCommand

models_to_export = [
    'auth',
    'users',
    'common',
    'content',
]


class Command(BaseCommand):
    hellp = 'Dumps Basic Data to make the App Work'

    def handle(self, **kwargs):
        dump_options = {
            'natural_foreign': True,
            'natural_primary': True,
            'indent': 4,
            'output': 'fixtures/data.json',
            'exclude': [
                'contenttypes',
                'admin'
            ],
        }
        call_command('dumpdata', *models_to_export, **dump_options)