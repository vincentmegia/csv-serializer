from decorator.csvloader import csv_loader


@csv_loader(filepath="./test.csv", entity="model.order.Order")
class Loader():
    def __init__(self):
        pass

    def load(self, list):


        print("test")
        pass
