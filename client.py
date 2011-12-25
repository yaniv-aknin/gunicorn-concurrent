#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import httplib

import argparse
import requests

def main(options):
    request_handles = []
    for request_number in range(options.concurrent_requests):
        request_handles.append(requests.get("http://localhost:%d/" % (options.port),
                                            params=dict(nbytes=options.nbytes)))
    for index, request in enumerate(request_handles):
        try:
            print("OK:  got %d bytes for request %d" % (len(request.content), index))
        except httplib.IncompleteRead, error:
            print("BAD: got %d bytes for request %d" % (len(error.partial[0]), index))

if __name__ == '__main__':
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) # make stdout unbuffered
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=5000, type=int)
    parser.add_argument("-c", "--concurrent-requests", default=1, type=int)
    parser.add_argument("-n", "--bytes-per-response", default=2**20, type=int, dest='nbytes')
    options = parser.parse_args()
    main(options)
