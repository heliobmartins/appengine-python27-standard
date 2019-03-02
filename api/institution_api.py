import endpoints
from google.appengine.ext import ndb
from protorpc import remote, message_types

from domain.institution_domain import Institution
from messages.institution_converter import convert_entity_into_to
from messages.institution_messages import InstitutionResponse, InstitutionRequest, InstitutionList
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

    @endpoints.method(message_types.VoidMessage,
                      InstitutionList,
                      path='list', http_method="GET",
                      name='list')
    def list(self, request):
        institutions = Institution.query().fetch()
        institutions_converted = []
        for institution in institutions:
            converted = convert_entity_into_to(institution)
            institutions_converted.append(converted)

        return InstitutionList(items=[institution_to for institution_to in institutions_converted])
