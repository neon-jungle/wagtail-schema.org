from __future__ import absolute_import, unicode_literals

import django
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

try:
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail.core import urls as wagtail_urls
    from wagtail.documents import urls as wagtaildocs_urls
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailadmin import urls as wagtailadmin_urls
    from wagtail.wagtailcore import urls as wagtail_urls
    from wagtail.wagtaildocs import urls as wagtaildocs_urls


# Include admin URLs correctly based on django version
if django.VERSION[0] > 1 or (django.VERSION[0] == 1 and django.VERSION[1] >= 9):
    urlpatterns = [
        url(r'^django-admin/', admin.site.urls),
    ]
else:
    urlpatterns = [
        url(r'^django-admin/', include(admin.site.urls)),
    ]

urlpatterns += [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
