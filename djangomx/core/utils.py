# coding: utf-8
from datetime import datetime

from django.utils.text import slugify


def get_filename(extension):
    """
    Returns a unique file name based on its extension parameter
    """
    ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return '%s%s' % (ts, extension)


def truncated_slugify(string, max_length=75):
    """
    Returns a slug, excludes keywords and truncates it to a default of 75 characters.
    """
    if len(string) > max_length:
        truncated_string = ''
        for word in string.split(' '):
            next_len = len(truncated_string) + len(word)
            if next_len < max_length:
                truncated_string += '{0}{1}'.format(word, ' ')
            elif next_len == max_length:
                truncated_string += '{0}'.format(word)
                break

        string = truncated_string.strip(' ')

    return slugify(string)
