__author__ = 'Nacho-w7'

from unittest import TestCase
from src.controllers.DataLoader import DataLoader


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