from django.db import models


class CommaSeparatedField(models.CharField):
    """ Usable as select widget with multiple values. """

    def from_db_value(self, value, expression, connection):
        print("from DB: ", value)
        if value:
           return value.split(',')
        return []

    def get_prep_value(self, obj):
        return ",".join(obj)

    def to_python(self, value):
        return value
