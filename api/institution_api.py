import endpoints
from protorpc import remote, message_types

from messages.institution_messages import InstitutionResponse, InstitutionRequest, InstitutionList, InstitutionCode
from services.institution_service import InstitutionService
from .api_definition import api_definition


@api_definition.api_class(resource_name='institution', path='institution')
class InstitutionApi(remote.Service):
    _service = InstitutionService.get_instance()

    @endpoints.method(InstitutionRequest,
                      InstitutionResponse,
                      path='new', http_method='POST',
                      name='new')
    def new(self, request):
        institution = InstitutionRequest(name=request.name,
                                         code=request.code,
                                         logo=request.logo)

        return self._service.create(institution)

    @endpoints.method(message_types.VoidMessage,
                      InstitutionList,
                      path='list', http_method="GET",
                      name='list')
    def list(self, _):
        institutions_list = self._service.list_all_entities()
        return InstitutionList(institutions=[institution_to for institution_to in institutions_list])

    @endpoints.method(InstitutionCode,
                      InstitutionList,
                      path='listByCode/{code}', http_method="GET",
                      name='listByCode')
    def search(self, request):
        institutions_list = self._service.list_entities_by_code(code=request.code)
        return InstitutionList(institutions=[institution_to for institution_to in institutions_list])