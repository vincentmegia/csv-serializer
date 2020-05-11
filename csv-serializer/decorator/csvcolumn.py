import functools


class CsvColumn(object):
    """
    Decorator to be set to the setter of the entity, this will tell the framework which
    fields are to be populated
    """
    _fields = []

    def __init__(self, key, type):
        self._key = key
        self._type = type

    def __get__(self, obj, type=None):
        return functools.partial(self, obj)

    def __call__(self, *args, **kwargs):
        if not hasattr(self, 'fn'):
            self._fn = args[0]
            return self
        self._fn(*args, **kwargs)

    def __set_name__(self, owner, name):
        self._fields.append({"key": self._key, "method": name, "type": self._type})
        self._fn.class_name = owner.__name__
        setattr(owner, name, self._fn)

    @classmethod
    def get_fields(cls):
        """

        :return:
        """
        return cls._fields

    @classmethod
    def get_field(cls, key):
        """

        :param key:
        :return:
        """
        return [field for field in cls._fields if key == field["key"]]
