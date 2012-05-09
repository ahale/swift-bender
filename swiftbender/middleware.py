from webob import Response
import random

from quotes import benderism

class Bender(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, env, start_response):
        def _start_response(status, headers, exc_info=None):
            quote = benderism[random.randrange(0,len(benderism))]
            #headers = dict(headers).items()
            headers.append(('X-Bender', quote))
            return start_response(status, headers, exc_info)
        return self.app(env, _start_response)

def filter_factory(global_conf, **local_conf):
    """
    paste.deploy app factory for creating WSGI proxy apps.
    """
    def bender_filter(app):
        return Bender(app)
    return bender_filter
