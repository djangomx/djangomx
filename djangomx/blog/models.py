#coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

from tinymce.models import HTMLField

from userdj.models import User

class Category(models.Model):
    """
    Category Model
    """
    title = models.CharField(verbose_name=_(u'Título'), help_text=_(u' '), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), help_text=_(u'Identificador Uri'), max_length=255, unique=True)
    description = models.CharField(verbose_name=_(u'Descripción'), help_text=_(u' '), max_length=255, blank=True)

    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')

    def __unicode__(self):
        return "%s" % (self.title,)


class Post(models.Model):
    """
    Post Model
    """
    title = models.CharField(verbose_name=_(u'Título'), help_text=_(u' '), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), help_text=_(u'Identificador Uri'), max_length=255, unique=True)
    content = HTMLField()
    extract = HTMLField(blank=True, help_text=_(u'Texto para el resumen'))
    image = models.ImageField(blank=True, upload_to="blog")
    category = models.ForeignKey(Category, verbose_name=_(u'Categoría'), null=True, blank=True)
    author = models.ForeignKey(User, verbose_name=_(u'Autor'))
    date_publish = models.DateTimeField(verbose_name=_(u'Fecha de Publicación'))

    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Posts')
        verbose_name_plural = _(u'Posts')

    def __unicode__(self):
        return "%s" % (self.title,)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
