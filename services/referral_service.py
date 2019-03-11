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

    def delete(self, request):
        referral = Referral.get_by_id(request.id)
        referral.key.delete()
        return Referral.encode(referral)

    def update(self, request):
        referral = self._does_referral_exist(request.id)
        return Referral.encode(self._validate_update(request, referral)
                               .put()
                               .get())

    def _validate_entity_creation(self, new_referral):
        if not normalize_email(new_referral.email):
            raise endpoints.BadRequestException("Invalid email entry")

    def _does_referral_exist(self, id):
        key = ndb.Key(Referral, id)
        referral = key.get()
        if referral is None:
            raise endpoints.BadRequestException("Could not find the referral.")
        return referral

    def _save(self, new_referral):
        return Referral.encode(
                Referral.decode(new_referral)
                .put()
                .get())

    def _validate_update(self, request, referral):
        # What if the user has 30 properties. How would you address something so big?
        if request.claim_number is not None:
            referral.claim_number = request.claim_number
        if request.new_name is not None:
            referral.name = request.new_name
        if request.new_email is not None:
            referral.email = request.new_email
        if request.new_phone is not None:
            referral.phone = request.new_phone
        if request.new_consent is not None:
            referral.consent = request.new_consent
        return referral

