"""RPC Messages module."""
import endpoints
from protorpc import messages as m


class ReferralRequest(m.Message):
    name = m.StringField(1, required=True)


class ReferralResponse(m.Message):
    name = m.StringField(1)
