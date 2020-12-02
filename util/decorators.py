import time
from flask import Flask, jsonify, request
import traceback

def timer(f):
    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        # print ('func:%r args:[%r, %r] took: %2.4f sec' % \
        #   (f.__name__, args, kw, te-ts))
        print ('func:%r took: %2.4f sec' % \
          (f.__name__, te-ts))
        return result
    return timed

def debug(f):
    def timed(*args, **kw):
        print('entering',f.__name__ )
        try:
            result = f(*args, **kw)
        except:
            print(f.__name__, "failed with args: ", *args, kw)
            traceback.print_exc()
            raise
        print('exiting', f.__name__)
        return result
    return timed

# @debug
# def test(a, b, c, keyarg=0):
#     a = {}
#     b = a['test']

