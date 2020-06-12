import mongoengine

class ModelA(mongoengine.Document):
    meta = {'collection': 'module_two_model_a'}
    name = mongoengine.StringField()
    b_reference = mongoengine.ReferenceField('ModelB')


class ModelB(mongoengine.Document):
    meta = {'collection': 'module_two_model_b'}
    name = mongoengine.StringField()
    a_reference = mongoengine.ReferenceField('ModelA')
