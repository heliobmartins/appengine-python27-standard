from google.appengine.ext import ndb


class Referral(ndb.Model):
    # This is where we map the entities to Datastore.
    claim_number = ndb.IntegerProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    consent = ndb.BooleanProperty()
    institution_id = ndb.IntegerProperty()
