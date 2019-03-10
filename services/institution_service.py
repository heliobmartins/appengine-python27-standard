from google.appengine.ext.ndb import Cursor

from domain.institution.institution_domain import Institution
from domain.institution.institution_messages import InstitutionListResponse


class InstitutionService(object):
    __instance = None

    def __init__(self):
        if InstitutionService.__instance is not None:
            raise Exception("This class is a Singleton")
        else:
            InstitutionService.__instance = self

    @classmethod
    def get_instance(cls):
        if InstitutionService.__instance is None:
            InstitutionService()
        return InstitutionService.__instance

    def create(self, new_institution):
        self._validate_entity_creation(new_institution)
        return self._save(new_institution)

    def list_entities_by_code(self, request):
        cursor = Cursor(urlsafe=request.cursor)
        query = Institution.query()
        print"\n\n\n"
        print request
        if request.code:
            query = Institution.query(Institution.code == request.code)
        institutions, next_cursor, more = query.fetch_page(page_size=request.page_size, start_cursor=cursor)
        response = InstitutionListResponse()
        response.institutions = [Institution.encode(i) for i in institutions]
        if more and next_cursor:
            response.cursor = next_cursor.urlsafe()
        return response

    def _validate_entity_creation(self, new_institution):
        pass
        # raise endpoints.BadRequestException("Error while creating Institution")

    def _save(self, new_institution):
        return Institution.encode(
            Institution.decode(new_institution)
            .put()
            .get())
