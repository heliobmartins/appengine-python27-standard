import endpoints
from protorpc import remote

from messages.institution_messages import InstitutionId
from messages.referral_messages import ReferralRequest, ReferralResponse, ReferralResponseList
from services.referral_service import ReferralService
from .api_definition import api_definition


@api_definition.api_class(resource_name='referral', path='referral')
class ReferralApi(remote.Service):
    _service = ReferralService.get_instance()

    @endpoints.method(ReferralRequest,
                      ReferralResponse,
                      path='new', http_method='POST',
                      name='new')
    def new(self, request):
        # TODO 1: How can I instead of add name=request.name + all other fields as parameter, add somethin such: User added?
        # TODO 2: Where would be good to create validations services, such as UTIL (validate email, phone, etc which cna be reused)?
        # TODO 3: How to handle errors, such as 404, 503, 400 etc?
        # TODO 4: Example of setup to NDB using Datastore?
        referral = ReferralRequest(claim_number=request.claim_number,
                                   name=request.name,
                                   email=request.email,
                                   phone=request.phone,
                                   consent=request.consent,
                                   institution_id=request.institution_id)

        return self._service.create(referral)

    # TODO: Marcot, Essa API pode usar mensagens de outras entidades?
    @endpoints.method(InstitutionId,
                      ReferralResponseList,
                      path='listByCode/{id}', http_method="GET",
                      name='listByCode')
    def search(self, request):
        referral_list = self._service.fetch_referrals_from_institutions(id=request.id)
        return ReferralResponseList(referrals=[referral_to for referral_to in referral_list])
