__author__ = 'ezequiel'

from src.entities.agents.Agent import Agent
from src.entities.base.Article import Article
from src.entities.base.SaleLine import SaleLine
from src.entities.base.Sale import Sale
from src.entities.agents.Commission import Commission

from unittest import TestCase


class TestAgent(TestCase):
    """
    Test class that aims to test the most interesting methods from Agent class

    """

    def test_get_commissions(self):
        """
        Test get_commissions() method
        get_commissions() is the most important method in Agent and it also has a certain complexity. This test
        aims to find bugs in an early stage.

        """

        a1 = Agent("A-001", "Paco", "Martin", "1/1/1990", 200.0, "pmartin@samplecompany.com")
        art1 = Article("123776789087", "Article 1", 1.0, 10.0)
        c1 = Commission("Commission 10%", 0.1)
        art1.set_commission(c1)

        sale = a1.create_sale()
        line = SaleLine(1, art1)
        sale.add_line(line)

        self.assertEqual(a1.get_commissions(), 1)

        sale2 = a1.create_sale()
        line1 = SaleLine(1, art1)
        sale2.add_line(line1)

        self.assertEqual(a1.get_commissions(), 2)
