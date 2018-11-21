import endpoints
from protorpc import remote

from messages import referral_messages
from .api_definition import api_definition


@api_definition.api_class(resource_name='referral', path='referral')
class ReferralApi(remote.Service):

    @endpoints.method(referral_messages.ReferralRequest,
                      referral_messages.ReferralResponse,
                      path='referral', http_method='GET',
                      name='referral')
    def echo(self, request):
        return referral_messages.ReferralResponse(name=request.name)
