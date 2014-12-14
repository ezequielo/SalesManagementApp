__author__ = 'Nacho-w7'

from unittest import TestCase
from src.controllers.DataLoader import DataLoader
from datetime import date


class TestOrganization(TestCase):
    """

    Test organization
    Testing method more important of Organization

    """
    def test_best_agent(self):
        """

        Validate method best agent

        """
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
        num_max = 0.0
        best_agent = None
        for agent in org.agent_list:
            if agent.get_total() > num_max:
                num_max = agent.get_total()
                best_agent = agent.agent_id
        self.assertEqual(best_agent, "A-003")

    def test_annual_balance(self):
        """

        TestAnnual balance
        Given a year, this method can return the total revenue of the year

        """
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
        year = date.today().year
        self.assertEqual(org.annual_balance(year), 86.9)

    def test_quarter_balance(self):
        """

        TestAnnual balance
        Given a year, this method can return the total revenue of the year

        """
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
        year = date.today().year
        self.assertEqual(org.quarter_balance(year,4),86.9)