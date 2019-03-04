import endpoints

from domain.institution_domain import Institution
from messages.institution_converter import convert_to_into_entity, convert_entity_into_to


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
        institution = convert_to_into_entity(new_institution)
        if institution.put():
            return convert_entity_into_to(institution)
        raise endpoints.BadRequestException

    def list_all_entities(self):
        institutions = Institution.query().fetch()
        institutions_converted = []
        for institution in institutions:
            converted = convert_entity_into_to(institution)
            institutions_converted.append(converted)
        return institutions_converted
