import endpoints
from protorpc import remote

from domain.institution.institution_messages import InstitutionResponse, InstitutionRequest, InstitutionListResponse, \
    InstitutionsRequest
from services.institution_service import InstitutionService
from .api_definition import api_definition


@api_definition.api_class(resource_name='institutions', path='institutions')
class InstitutionApi(remote.Service):
    _service = InstitutionService.get_instance()

    @endpoints.method(InstitutionRequest,
                      InstitutionResponse,
                      path='new', http_method='POST',
                      name='new')
    def new(self, request):
        return self._service.create(request)

    @endpoints.method(InstitutionsRequest,
                      InstitutionListResponse,
                      path='list/{code}', http_method="GET",
                      name='list')
    def search(self, request):
        return self._service.list_entities_by_code(request)
