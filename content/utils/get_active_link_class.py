from django.conf import settings
from django.utils.encoding import escape_uri_path


def get_active_link_class(urls, request) -> str:
    request_path = escape_uri_path(request.path)
    css_active_class = getattr(settings, "ACTIVE_LINK_CSS_CLASS", "active")
    css_inactive_class = getattr(settings, "ACTIVE_LINK_CSS_INACTIVE_CLASS", "")
    active = request_path.startswith(urls) or urls.startswith(request_path)
    active_link_class = css_active_class if active else css_inactive_class
    return active_link_class