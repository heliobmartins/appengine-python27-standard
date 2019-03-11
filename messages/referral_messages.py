"""RPC Messages module."""
from protorpc import messages as m

from messages.institution_messages import InstitutionResponse


class ReferralRequest(m.Message):
    claim_number = m.IntegerField(1, required=True)
    name = m.StringField(2, required=True)
    email = m.StringField(3, required=True)
    phone = m.StringField(4, required=True)
    consent = m.BooleanField(5, required=True)
    institution_id = m.IntegerField(6, required=True)


class ReferralResponse(m.Message):
    claim_number = m.IntegerField(1)
    name = m.StringField(2)
    email = m.StringField(3)
    phone = m.StringField(4)
    consent = m.BooleanField(5)
    institution = m.MessageField(InstitutionResponse, 6)


class ReferralIdRequest(m.Message):
    id = m.IntegerField(1, required=True)


class ReferralListByInstitutionRequest(m.Message):
    institution_id = m.IntegerField(1, required=True)
    cursor = m.StringField(2)
    page_size = m.IntegerField(3, required=True, default=25)


class ReferralListResponse(m.Message):
    referrals = m.MessageField(ReferralResponse, 1, repeated=True)
    cursor = m.StringField(2)
