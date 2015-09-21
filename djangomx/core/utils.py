# coding: utf-8
from datetime import datetime


def get_filename(extension):
    """
    Returns a unique file name based on its extension parameter
    """
    ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return '%s%s' % (ts, extension)
