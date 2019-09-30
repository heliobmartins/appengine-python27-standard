import os

import google
from google.appengine.ext import vendor

lib_directory = os.path.dirname(__file__) + '/lib'
# Change where to find the google package (point to the lib/ directory)
google.__path__ = [os.path.join(lib_directory, 'google')] + google.__path__
vendor.add(lib_directory)


def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app

try:
    from google.appengine.tools.devappserver2.python.runtime.stubs import FakeFile
    FakeFile._allowed_dirs.update(['/System/Library/CoreServices/'])
except ImportError:
    pass