import endpoints

from messages.referral_converter import convert_to_into_entity, convert_entity_into_to
from messages.referral_messages import ReferralResponse
from utils.caas_utils import normalize_email


class ReferralService(object):
    @staticmethod
    def create(new_referral):
        normalized_email = normalize_email(new_referral.email)
        if normalized_email:
            referral = convert_to_into_entity(new_referral)
            referral.email = normalized_email
            referral.put()
            return convert_entity_into_to(referral)
        # TODO: How can I change the code error? 502 or something.
        raise endpoints.BadRequestException
