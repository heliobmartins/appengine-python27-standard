import endpoints
from protorpc import remote

from messages.institution_messages import InstitutionResponse, InstitutionRequest
from services.institution_service import InstitutionService
from .api_definition import api_definition


@api_definition.api_class(resource_name='institution', path='institution')
class InstitutionApi(remote.Service):
    service = InstitutionService()

    @endpoints.method(InstitutionRequest,
                      InstitutionResponse,
                      path='new', http_method='POST',
                      name='new')
    def new(self, request):
        institution = InstitutionRequest(name=request.name,
                                         code=request.code,
                                         logo=request.logo)

        return InstitutionApi.service.create(institution)
