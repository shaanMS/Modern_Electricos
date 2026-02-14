from django.db import models

class AddressField(models.Field):
    description = "PostgreSQL composite address_type"

    def db_type(self, connection):
        return "address_type"

    def from_db_value(self, value, expression, connection):
        return value

    def get_prep_value(self, value):
        return value
