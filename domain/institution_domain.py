from google.appengine.ext import ndb


class Institution(ndb.Model):
    name = ndb.StringProperty()
    code = ndb.StringProperty()
    logo = ndb.StringProperty()

