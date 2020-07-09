import unittest
from printer  import Printer

class Test_Printer(unittest.TestCase):

    def test_printer_available(self):
        printer=Printer()
        self.assertTrue(printer.printer_available())
        printer.add_print_job('tarea')
        self.assertTrue(printer.print_job)
    
    def test_printer_not_available(self):
        printer=Printer()
        printer.add_print_job('tarea')
        printer.print_job()
        self.assertFalse(printer.printer_available())

    def test_printer_nothing_print(self):
        printer=Printer()
        printer.print_job()
        self.assertTrue(printer.error_flag)
        self.assertEqual(printer.error_description,"nothing to print")
    
    def test_queue_printer(self):
        printer=Printer()
        self.assertTrue(printer.printer_available())
        printer.add_print_job('tarea1')
        printer.add_print_job('tarea2')
        printer.print_job()
        self.assertFalse(printer.printer_available())
        printer.reset_printer()
        self.assertTrue(printer.printer_available())


if __name__ == '__main__':
   unittest.main()