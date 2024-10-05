TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'width': '100%',
    'plugins': (
        'advlist autolink lists link image charmap print preview hr anchor pagebreak '
        'searchreplace wordcount visualblocks visualchars code fullscreen '
        'insertdatetime media nonbreaking save table directionality '
        'emoticons template paste textpattern imagetools'
    ),
    'toolbar1': (
        'fullscreen preview bold italic underline | fontselect, fontsizeselect | '
        'forecolor backcolor | alignleft aligncenter alignright alignjustify | '
        'indent outdent | bullist numlist | table | link image media | code'
    ),
    'toolbar2': 'undo redo | cut copy paste | searchreplace | charmap emoticons',
    'image_advtab': True,  # Enable the Advanced tab for images
    'file_picker_callback': 'function(callback, value, meta) { filebrowser(callback, value, meta); }',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}
