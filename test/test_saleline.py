__author__ = 'ezequiel'

from mockito import *
from unittest import TestCase
from src.entities.base.SaleLine import SaleLine
from src.entities.base.Article import Article

class TestSaleLine(TestCase):
    """
    Test sale line
    Test class for testing the most interesting method of SaleLine class

    """

    def test_get_subtotal(self):
        """
        Test get_subtotal()
        This method aims to find bugs in the get_subtotal() function
        
        """

        article = mock(Article)
        when(article).get_list_price().thenReturn(20.0)

        line = SaleLine(2, article)

        self.assertEqual(line.get_subtotal(), 40.0)