import endpoints
from google.appengine.ext import ndb

from domain.institution_domain import Institution
from domain.referral_domain import Referral
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
            # TODO: @Marco Tulio Qual a maneira correta de fazer?
            # Olha como estao minhas importacoes de NDB, etc.. isso ta dando um no na minha cabeca.

            # referral.institution_code = institution_query.code

            # Option 1
            #institution_query = Institution.get_by_id(new_referral.institution_id)
            #referral.institution_id = institution_query.code

            # Option 2
            institution = Institution.get_by_id(new_referral.institution_id)
            referral_id = referral.allocate_ids(size=1, parent=institution.key)[0]
            referral_key = ndb.Key(Referral, referral_id, parent=institution.key)
            referral.key = referral_key
            referral.put()


            return convert_entity_into_to(referral)
        # TODO: How can I change the code error? 502 or something.
        raise endpoints.BadRequestException

    def fetch_referrals_from_institutions(self, id):
        q = Referral.query(ancestor=ndb.Key(Institution, id))
        referral_converted = []
        for referral in q:
            print referral
            converted = convert_entity_into_to(referral)
            referral_converted.append(converted)

        return referral_converted
