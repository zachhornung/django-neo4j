from neomodel import RelationshipTo, StringProperty, StructuredNode, UniqueIdProperty

# Create your models here.


class Question(StructuredNode):
    uid = UniqueIdProperty()
    prompt = StringProperty(required=True)


class Choice(StructuredNode):
    uid = UniqueIdProperty()
    text = StringProperty(unique=True)

    question = RelationshipTo("Question", "QUESTION")
