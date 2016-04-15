import time


def timeit(method):
    """
    Decorator for measuring the execution time of methods
    Example:
    @timed
    def foo():
        print map(lambda x: x*1000, range(10000))
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print '%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts)
        return result

    return timed
