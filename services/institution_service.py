import endpoints

from messages.institution_converter import convert_to_into_entity, convert_entity_into_to


class InstitutionService(object):
    @staticmethod
    def create(new_institution):
        institution = convert_to_into_entity(new_institution)
        if institution.put():
            return convert_entity_into_to(institution)
        raise endpoints.BadRequestException
