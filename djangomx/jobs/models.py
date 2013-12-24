#coding: utf-8
import os
from django.db import models
from datetime import datetime


def get_filename(extension):
    """ Returns a unique file name based on its extension """
    ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return '%s%s' % (ts, extension)


def get_upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    return 'jobs-images/%s' % get_filename(ext)


class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=400)
    contact = models.EmailField()

    active = models.BooleanField(default=True)
    aproved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
