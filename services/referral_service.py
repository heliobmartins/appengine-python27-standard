import endpoints

from domain.institution_domain import Institution
from messages.referral_converter import convert_to_into_entity, convert_entity_into_to
from utils.caas_utils import normalize_email


class ReferralService:
    __instance = None

    def __init__(self):
        if ReferralService.__instance is not None:
            raise Exception("This class is a Singleton")
        else:
            ReferralService.__instance = self

    @classmethod
    def get_instance(cls):
        if ReferralService.__instance is None:
            ReferralService()
        return ReferralService.__instance

    def create(self, new_referral):
        normalized_email = normalize_email(new_referral.email)
        if normalized_email:
            referral = convert_to_into_entity(new_referral)
            referral.email = normalized_email
            #TODO: Is this correct?
            institution_query = Institution.get_by_id(new_referral.institution_code)
            referral.institution_code = institution_query.code
            referral.put()
            return convert_entity_into_to(referral)
        # TODO: How can I change the code error? 502 or something.
        raise endpoints.BadRequestException
