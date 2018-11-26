from google.appengine.ext import ndb


class ReferralStore(ndb.Model):
    claim_number = ndb.IntegerProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    consent = ndb.BooleanProperty()

