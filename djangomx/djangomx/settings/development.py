from common import *
try:
    from .local_settings import *
except ImportError as e:
    print "error local_settinga"
    raise ImportError
