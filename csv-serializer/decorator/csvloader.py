import csv
from tools.activator import Activator
from decorator.csvcolumn import CsvColumn


def csv_loader(filepath, entity):
    """
    Decorator for loader, a loader simply reads the csv file and hydrates your entities
    Entities must be decorated with @csv_column for the entities to be populated correctly
    :param filepath:
    :param entity:
    :return:
    """
    def csv_decorator(function):
        def wrapper():
            records = []
            entitylist = []

            try:
                with open(filepath) as csv_file:
                    reader = csv.reader(csv_file, delimiter=',', quotechar='|')
                    for index, row in enumerate(reader):
                        if index == 0:
                            header_row = row
                            continue
                        item = [{"key": header_row[i], "value": item} for i, item in enumerate(row)]
                        records.append(item)
            except Exception as e:
                raise Exception(e)

            for record in records:
                instance = Activator.get_instance(entity)
                for item in record:
                    field = CsvColumn.get_field(item["key"])
                    if len(field) == 0:
                        continue
                    value = item["value"]
                    if not isinstance(value, field[0]["type"]):
                        print("error")
                    method = field[0]["method"]
                    getattr(instance, method)(instance, value)
                entitylist.append(instance)
            function().load(entitylist)
        return wrapper
    return csv_decorator
