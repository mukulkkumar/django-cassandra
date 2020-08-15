from django_cassandra_engine.rest.serializers import DjangoCassandraModelSerializer
from .models import Person


class PersonSerializer(DjangoCassandraModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
