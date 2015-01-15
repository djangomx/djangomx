#coding: utf-8
import os
from django.db import models
from django.utils.translation import ugettext as _
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

from tinymce.models import HTMLField
from utilities.utils import get_filename
from user_django.models import User


class Category(models.Model):
    """ Category Model """
    title = models.CharField(
        verbose_name=_(u'Título'),
        help_text=_(u' '),
        max_length=255
    )
    slug = models.SlugField(
        verbose_name=_(u'Slug'),
        help_text=_(u'Identificador Uri'),
        max_length=255,
        unique=True
    )
    description = models.CharField(
        verbose_name=_(u'Descripción'),
        help_text=_(u' '),
        max_length=255,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')

    def __unicode__(self):
        return "%s" % (self.title,)


def get_img_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return 'blog/%s' % get_filename(ext)


class Post(models.Model):
    """ Post Model """
    title = models.CharField(
        verbose_name=_(u'Título'),
        help_text=_(u' '),
        max_length=255
    )
    slug = models.SlugField(
        verbose_name=_(u'Slug'),
        help_text=_(u'Identificador Uri'),
        max_length=255,
        unique=True
    )
    image = models.ImageField(
        verbose_name=_(u'Imágen'),
        help_text=_(u'Imagen destacada'),
        blank=True,
        upload_to=get_img_path
    )
    content = HTMLField()
    extract = HTMLField(blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name=_(u'Categoría'),
        null=True,
        blank=True
    )
    author = models.ForeignKey(User, verbose_name=_(u'Autor'))
    published_at = models.DateTimeField(
        verbose_name=_(u'Fecha de publicación')
    )
    likes = models.PositiveIntegerField(verbose_name=_(u'Likes'), default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Posts')
        verbose_name_plural = _(u'Posts')
        ordering = ["-created_at"]

    def __unicode__(self):
        return "%s" % (self.title,)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse(
            "admin:%s_%s_change" % (
                content_type.app_label, content_type.model
            ),
            args=(self.id,)
        )
