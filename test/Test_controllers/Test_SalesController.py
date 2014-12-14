__author__ = 'Nacho-w7'

from unittest import TestCase
from mockito import *
from src.controllers.DataLoader import DataLoader
from src.entities.agents.Agent import Agent


class Test_SalesController(TestCase):
    def test_select_agent_true(self):
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
        org.get_agent_list()
        ag = mock(Agent)
        when(ag).get_agent_id().thenReturn("A-001")
        boolean = False
        for agent in org.agent_list:
            if agent.agent_id == ag.get_agent_id():
                boolean = True
        self.assertEquals(boolean, True)

    def test_select_agent_false(self):
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
        org.get_agent_list()
        ag1 = mock(Agent)
        when(ag1).get_agent_id().thenReturn(None)
        boolean = False
        for agent in org.agent_list:
            if agent.agent_id == ag1.get_agent_id():
                boolean = True
            self.assertEquals(boolean, False)
    manage_sales(mc, org)