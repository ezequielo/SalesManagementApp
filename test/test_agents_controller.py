__author__ = 'Nacho-w7'
from unittest import TestCase
from src.entities.agents.Agent import Agent
from src.entities.org.Organization import Organization
from src.controllers.AgentController import AgentController

class Test_SalesController(TestCase):

    def test_list_agents(self):
        a1 = Agent("A-001", "Paco", "Martin", "1/1/1990", 200.0, "pmartin@samplecompany.com")
        o = Organization("ORG0001", "SampleCompany")
        o.add_agent(a1)
        o.remove_agent(a1)
        self.assertIsNone(AgentController.list_agents(o),True)