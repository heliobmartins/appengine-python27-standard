import endpoints
from protorpc import remote

from messages import referral_messages
from .api_definition import api_definition


@api_definition.api_class(resource_name='referral', path='referral')
class ReferralApi(remote.Service):

    @endpoints.method(referral_messages.ReferralRequest,
                      referral_messages.ReferralResponse,
                      path='new', http_method='POST',
                      name='new')
    def new(self, request):
        #TODO 1: How can I instead of add name=request.name + all other fields as parameter, add somethin such: User added?
        #TODO 2: Where would be good to create validations services, such as UTIL (validate email, phone, etc which cna be reused)?
        #TODO 3: How to handle errors, such as 404, 503, 400 etc?
        #TODO 4: Example of setup to NDB using Datastore?
        return referral_messages.ReferralResponse(name=request.name + ' successfully joined the program.')
