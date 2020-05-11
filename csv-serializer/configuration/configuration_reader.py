import json
from configuration.serializer import Serializer


class ConfigurationReader:
    def __init__(self):
        with open("./config.json") as json_file:
            self.serializers = []
            data = json.load(json_file)
            for serializer in data["serializers"]:
                self.serializers.append(Serializer(**serializer))
