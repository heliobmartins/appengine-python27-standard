from domain.institution_domain import Institution
from messages.institution_messages import InstitutionResponse


def convert_entity_into_to(institution):
    return InstitutionResponse(name=institution.name,
                               code=institution.code,
                               logo=institution.logo)


def convert_to_into_entity(institution_to):
    return Institution(name=institution_to.name,
                       code=institution_to.code,
                       logo=institution_to.logo)
