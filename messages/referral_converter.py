from domain.referral_domain import Referral
from messages.referral_messages import ReferralResponse


def convert_entity_into_to(referral):
    return ReferralResponse(claim_number=referral.claim_number,
                            name=referral.name,
                            email=referral.email,
                            phone=referral.phone,
                            consent=referral.consent)


def convert_to_into_entity(referral_to):
    return Referral(claim_number=referral_to.claim_number,
                    name=referral_to.name,
                    email=referral_to.email,
                    phone=referral_to.phone,
                    consent=referral_to.consent)
