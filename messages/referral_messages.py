"""RPC Messages module."""
import endpoints
from protorpc import messages as m


class ReferralRequest(m.Message):
    claim_number = m.IntegerField(1, required=True)
    name = m.StringField(2, required=True)
    email = m.StringField(3, required=True)
    phone = m.StringField(4, required=True)
    consent = m.BooleanField(5, required=True)


class ReferralResponse(m.Message):
    claim_number = m.IntegerField(1)
    name = m.StringField(2)
    email = m.StringField(3)
    phone = m.StringField(4)
    consent = m.BooleanField(5)
