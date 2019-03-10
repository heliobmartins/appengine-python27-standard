from protorpc import messages as m


class InstitutionRequest(m.Message):
    name = m.StringField(1, required=True)
    code = m.StringField(2, required=True)
    logo = m.StringField(3)


class InstitutionResponse(m.Message):
    id = m.IntegerField(1)
    name = m.StringField(2)
    code = m.StringField(3)
    logo = m.StringField(4)


class InstitutionListResponse(m.Message):
    institutions = m.MessageField(InstitutionResponse, 1, repeated=True)
    cursor = m.StringField(2)


class InstitutionsRequest(m.Message):
    code = m.StringField(1)
    cursor = m.StringField(2)
    page_size = m.IntegerField(3, required=True, default=25)
