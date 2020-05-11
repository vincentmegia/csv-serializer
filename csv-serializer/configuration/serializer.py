class SerializerColumn():
    def __init__(self, *args):
        self.name = args[0]["name"]
        self.type = args[0]["type"]
        self.ordinal = args[0]["ordinal"]


class Serializer():
    def __init__(self, **kwargs):
        serializer = kwargs["serializer"]
        self.id = serializer["id"]
        self.columns = []
        for column in serializer["columns"]:
            self.columns.append(SerializerColumn(column))
