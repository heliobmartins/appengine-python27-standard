from google.appengine.ext import ndb


class Referral(ndb.Model):
    claim_number = ndb.IntegerProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    consent = ndb.BooleanProperty()

