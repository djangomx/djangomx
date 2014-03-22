from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'djangomx.views.home', name='home'),
    url(r'^subscribe', 'djangomx.views.subscribe_request', name='subscribe'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^contacto/', include('contact.urls')),
    url(r'^cursos/', include('courses.urls')),
    url(r'^ofertas/', include('jobs.urls')),

    url(r'^newsletter/', include('newsletter.urls')),

    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    url(
        r'^robots\.txt$',
        TemplateView.as_view(
            template_name='robots.txt', content_type='text/plain'
        )
    ),
    url(
        r'^sitemap\.xml$',
        TemplateView.as_view(
            template_name='sitemap.xml', content_type='text/xml'
        )
    ),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
