import endpoints
from protorpc import remote

from messages.referral_messages import ReferralRequest, ReferralResponse
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
                                   consent=request.consent)

        return self._service.create(referral)
