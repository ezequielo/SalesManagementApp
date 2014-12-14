__author__ = 'ezequiel'

from mockito import *
from unittest import TestCase
from src.entities.base.SaleLine import SaleLine
from src.entities.base.Sale import Sale


class TestSaleLine(TestCase):
    """
    Test sale line
    Test class for testing the most interesting method of SaleLine class

    """

    def test_get_total(self):
        """
        Test get_total()
        This method aims to find bugs in the get_total() function so that
        they can be fixed in an early stage of development

        """

        line1 = mock(SaleLine)
        line2 = mock(SaleLine)

        when(line1).get_subtotal().thenReturn(20.0)
        when(line2).get_subtotal().thenReturn(10.0)

        sale = Sale()
        sale.add_line(line1)
        sale.add_line(line2)

        self.assertEqual(sale.get_total(), 30.0)