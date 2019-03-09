from google.appengine.ext import ndb

from messages.referral_converter import convert_entity_into_to, convert_to_into_entity
from utils.caas_utils import normalize_email


class Referral(ndb.Model):
    claim_number = ndb.IntegerProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    consent = ndb.BooleanProperty()
    institution_id = ndb.KeyProperty()

    @staticmethod
    def encode(self):
        return convert_entity_into_to(self)

    @staticmethod
    def decode(referral_to):
        return convert_to_into_entity(referral_to)

    def _pre_put_hook(self):
        self.email = normalize_email(self.email)
