from __future__ import print_function

from urlparse import parse_qs
from time import time

workers = 1
loglevel = 'debug'
def pre_request(worker, req):
    req._start = time()
    worker.log.debug("%s starting request" % (worker,))
def post_request(worker, req, environ):
    worker.log.debug("%s finished request (%.2f secs)" % (worker, time() - req._start))

def wsgi(environ, start_response):
    nbytes = int(parse_qs(environ['QUERY_STRING']).get('nbytes', (2**20,))[0])
    start_response("200 OK", (
        ("Content-Length", str(nbytes)),
    ))
    return ['X' * nbytes]
