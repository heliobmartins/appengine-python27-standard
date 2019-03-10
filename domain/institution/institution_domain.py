from google.appengine.ext import ndb

from domain.institution.institution_converter import convert_entity_into_to, convert_to_into_entity


class Institution(ndb.Model):
    id = ndb.KeyProperty()
    name = ndb.StringProperty()
    code = ndb.StringProperty()
    logo = ndb.StringProperty()

    @staticmethod
    def encode(self):
        print(self)
        return convert_entity_into_to(self)

    @staticmethod
    def decode(institution_to):
        return convert_to_into_entity(institution_to)
