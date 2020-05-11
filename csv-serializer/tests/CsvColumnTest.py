import unittest
from decorator.csvcolumn import CsvColumn


class CsvColumnTest(unittest.TestCase):
    def test_csv_column(self):

        class Test(object):
            @CsvColumn(key="Row Id", type=type(int))
            def set_row_id(self):
                pass
        field = CsvColumn.get_field("Row Id")
        self.assertIsNotNone(field)

    def test_csv_column_type_int(self):
        class Test(object):
            #@CsvColumn("Order Id", type=int)
            def set_order_id(self, datatype=int):
                try:
                    if isinstance("asdf", datatype):
                        print("yes")
                    if (isinstance(1, datatype)):
                        print(1)
                except (Exception) as e:
                    print(e)
        Test().set_order_id()
