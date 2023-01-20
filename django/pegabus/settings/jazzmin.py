"""Jazzmin extension settings."""
from django.utils.translation import ugettext_lazy as _


JAZZMIN_SETTINGS = {
    'site_header': _('PEGABUS'),
    'topmenu_links': [
    ],
    "show_sidebar": True,
    # "show_ui_builder": True,
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Página Inicial",  "url": "home"},
    ],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "journal",
    "dark_mode_theme": None
}
