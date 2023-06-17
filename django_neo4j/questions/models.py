from neomodel import RelationshipTo, StringProperty, UniqueIdProperty

from django_neo4j.utils.django_neo4j import DjangoNode

# Create your models here.


class Question(DjangoNode):
    uid = UniqueIdProperty()
    prompt = StringProperty(required=True)


class Choice(DjangoNode):
    uid = UniqueIdProperty()
    text = StringProperty(unique=True)

    question = RelationshipTo("Question", "QUESTION")
