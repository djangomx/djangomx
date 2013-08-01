#coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _
from tinymce.models import HTMLField


class Type(models.Model):
    """
    Type Model: It is for types of proyects like freelance or in site
    """
    title = models.CharField(verbose_name=_(u'Título'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), help_text=_(u'Identificador Uri'), max_length=255, unique=True)

    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Tipo')
        verbose_name_plural = _(u'Tipos')

    def __unicode__(self):
        return "%s" % (self.title,)


class Skill(models.Model):
    """
    Skill Model:It is for types of skills like Python, Django, Vim, etc
    """
    title = models.CharField(verbose_name=_(u'Título'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), help_text=_(u'Identificador Uri'), max_length=255, unique=True)

    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Skill')
        verbose_name_plural = _(u'Skills')

    def __unicode__(self):
        return "%s" % (self.title,)


class Level(models.Model):
    """
    Level Model: It is for level of the proyect like beginner, intermedian, expert, etc
    """
    title = models.CharField(verbose_name=_(u'Título'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), help_text=_(u'Identificador Uri'), max_length=255, unique=True)

    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Nivel')
        verbose_name_plural = _(u'Niveles')

    def __unicode__(self):
        return "%s" % (self.title,)


class Project(models.Model):
    """
    Proyect model.
    """
    title = models.CharField(verbose_name=_(u'Título'), help_text=_(u'Título del proyecto'), max_length=255)
    image = models.ImageField(verbose_name=_(u'Imagen'), blank=True, upload_to='projects')
    place = models.CharField(verbose_name=_(u'Lugar'), help_text=_(u'Lugar del proyecto'), max_length=255)
    description = HTMLField()
    phone = models.PositiveIntegerField(verbose_name=_(u'Teléfono'), max_length=12, blank=True)
    email = models.EmailField(verbose_name=_(u'Email'), max_length=255)
    type_project = models.ForeignKey(Type)
    skills = models.ManyToManyField(Skill)
    level = models.ForeignKey(Level)

    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'Proyecto')
        verbose_name_plural = _(u'Proyectos')

    def __unicode__(self):
        return "%s" % (self.title,)