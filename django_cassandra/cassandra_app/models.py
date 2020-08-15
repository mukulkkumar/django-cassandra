# Create your models here.

import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class Person(DjangoCassandraModel):
    person_id = columns.Integer(primary_key=True, default=uuid.uuid4)
    firstName = columns.Text(index=True)
    lastName = columns.Text(index=True)
    gender = columns.Text(index=True)
    phone_number = columns.Text(index=True)
