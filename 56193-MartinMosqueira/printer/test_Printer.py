import unittest
from printer  import Printer

class Test_Printer(unittest.TestCase):
    def test_printer_available(self):
        result=Printer().printer_available()
        self.assertTrue(result)

    def print_job(self):
        result=Printer()
        result.add_print_job('hola')
        result1=result.error_flag
        self.assertFalse(result1)

if __name__ == '__main__':
   unittest.main()