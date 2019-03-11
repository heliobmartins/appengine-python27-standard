import endpoints
from protorpc import remote

from messages.referral_messages import ReferralRequest, ReferralResponse, ReferralListResponse, \
    ReferralListByInstitutionRequest, ReferralIdRequest, ReferralUpdateRequest
from services.referral_service import ReferralService
from .api_definition import api_definition


@api_definition.api_class(resource_name='referrals', path='referrals')
class ReferralApi(remote.Service):
    _service = ReferralService.get_instance()

    @endpoints.method(ReferralRequest,
                      ReferralResponse,
                      path='new', http_method='POST',
                      name='new')
    def new(self, request):
        return self._service.create(request)

    @endpoints.method(ReferralListByInstitutionRequest,
                      ReferralListResponse,
                      path='list/{institution_id}', http_method="GET",
                      name='list_by_institution')
    def search(self, request):
        return self._service.get_by_institution(request)

    @endpoints.method(ReferralIdRequest,
                      ReferralResponse,
                      path='delete', http_method='DELETE',
                      name="delete")
    def delete(self, request):
        return self._service.delete(request)

    @endpoints.method(ReferralUpdateRequest,
                      ReferralResponse,
                      path='update', http_method='PATCH',
                      name="update")
    def update(self, request):
        return self._service.update(request)
