import mongoengine
from modules import module_one
from modules import module_two

# When module_two is imported, it overwrites the _document_registry with the new clases (I think that's a bug)

if __name__ == "__main__":
    db = mongoengine.connect(db="mongoenginetest")
    a1 = module_one.ModelA(name='I am one A')
    a1.save()
    b1 = module_one.ModelB(name='I am one B', a_reference=a1)
    b1.save()
    # When the module_one.ModelB.a_reference class is being translated from the str "ModelA"
    # the _document_registry returns the module_two.ModelA class and the validation fails
    
    b2 = module_two.ModelB(name='I am two B')
    b2.save()
    a2 = module_two.ModelA(name='I am two A', b_reference=b2)
    a2.save()
