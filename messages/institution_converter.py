from messages.institution_messages import InstitutionResponse


def convert_entity_into_to(institution):
    return InstitutionResponse(id=institution.key.id(),
                               name=institution.name,
                               code=institution.code,
                               logo=institution.logo)


def convert_to_into_entity(institution_to):
    # TODO: @Marcot, e quando voce tem essa situacao? Importacao cruzada?
    from domain.institution_domain import Institution
    return Institution(name=institution_to.name,
                       code=institution_to.code,
                       logo=institution_to.logo)
