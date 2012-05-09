from webob import Response
import random

from benderisms import quote

class Bender(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, env, start_response):
        def _start_response(status, headers, exc_info=None):
            benderism = quote[random.randrange(0,len(quote))]
            headers = dict(headers).items()
            headers.append(('X-Bender', benderism))
            return start_response(status, headers, exc_info)
        return self.app(env, _start_response)

def filter_factory(global_conf, **local_conf):
    """
    paste.deploy app factory for creating WSGI proxy apps.
    """
    def bender_filter(app):
        return Bender(app)
    return bender_filter
