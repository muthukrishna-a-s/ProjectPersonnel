import django.db.models
from django.db.models import CharField


class Person(django.db.models.Model):
    username = CharField(max_length=200, null=True)
    first_name = CharField(max_length=200, null=True)
    last_name = CharField(max_length=200, null=True)
    email = CharField(max_length=200, null=True)
    phone_number = CharField(max_length=200, null=True)
    date_of_birth = CharField(max_length=200, null=True)
