import endpoints
from google.appengine.ext import ndb
from google.appengine.ext.ndb import Cursor

from domain.institution_domain import Institution
from domain.referral_domain import Referral
from messages.referral_messages import ReferralListResponse
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
        self._validate_entity_creation(new_referral)
        return self._save(new_referral)

    def get_by_institution(self, request):
        cursor = Cursor(urlsafe=request.cursor)
        referrals, next_cursor, more = Referral.query(
            Referral.institution_id == ndb.Key(Institution, request.institution_id)).fetch_page(
            page_size=request.page_size, start_cursor=cursor)
        response = ReferralListResponse()
        response.referrals = [Referral.encode(r) for r in referrals]
        if more and next_cursor:
            response.cursor = next_cursor.urlsafe()
        return response

    def _validate_entity_creation(self, new_referral):
        if not normalize_email(new_referral.email):
            raise endpoints.BadRequestException("Invalid email entry")

    def _save(self, new_referral):
        return Referral.encode(
                Referral.decode(new_referral)
                .put()
                .get())
