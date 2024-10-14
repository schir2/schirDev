import os

from django.conf import settings


def get_registered_icons(icon_directory='common/templates/cotton/icons'):
    icon_directory = os.path.join(settings.BASE_DIR, *icon_directory.split('/'))
    icon_list = []
    icon_directory_path = os.path.join(os.getcwd(), icon_directory)
    if os.path.exists(icon_directory_path):
        for file_name in os.listdir(icon_directory_path):
            if file_name.endswith('.html'):
                icon_name = file_name.replace('.html', '')
                icon_list.append(icon_name)
    return icon_list
