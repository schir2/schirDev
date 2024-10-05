CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Image', 'Link', 'Unlink', 'Anchor'],
            ['Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            ['Source'],
        ],
        'extraPlugins': ','.join(['uploadimage']),  # Enable image upload button
    }
}
