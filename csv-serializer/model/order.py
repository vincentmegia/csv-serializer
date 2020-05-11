from decorator.csvcolumn import CsvColumn


class Order(object):
    def __init__(self):
        self._id = None
        self._order_id = None

    @CsvColumn(key="Row Id", type=str)
    def set_id(self, id):
        self._id = id

    @CsvColumn(key="Order Id", type=str)
    def set_order_id(self, order_id):
        self._order_id = order_id
