__author__ = 'Nacho-w7'

from unittest import TestCase
from mockito import *
from src.controllers.DataLoader import DataLoader
from src.entities.agents.Agent import Agent
from src.controllers.SalesController import SalesController
from src.entities.base.Article import Article
class Test_SalesController(TestCase):
    def test_select_agent_true(self):
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
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
        ag1 = mock(Agent)
        when(ag1).get_agent_id().thenReturn(None)
        boolean = False
        for agent in org.agent_list:
            if agent.agent_id == ag1.get_agent_id():
                boolean = True
            self.assertEquals(boolean, False)

    def test_add_line_true(self):
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
        art_code = mock(Article)
        when(art_code).get_ean13().thenReturn("123776789087")
        boolean = False
        for category in org.categories:
            for article in category.article_list:
                if article.ean13 == art_code.get_ean13():
                    boolean = True
        self.assertEquals(boolean, True)

    def test_add_line_false(self):
        sample_data = DataLoader.load_sampledata()
        org = sample_data["organization"]
        art_code = mock(Article)
        when(art_code).get_ean13().thenReturn(None)
        boolean = False
        for category in org.categories:
            for article in category.article_list:
                if article.ean13 == art_code.get_ean13():
                    boolean = True
        self.assertEquals(boolean, False)