from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.views.generic.base import TemplateView, RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'djangomx.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/ico/favicon.ico')),
)

if settings.DEBUG:
    urlpatterns += patterns(staticfiles_urlpatterns(),
        ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
