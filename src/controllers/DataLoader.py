from src.entities.agents.Agent import Agent
from src.entities.agents.Commission import Commission
from src.entities.base.Article import Article
from src.entities.base.Category import Category
from src.entities.base.SaleLine import SaleLine
from src.entities.org.Organization import Organization
from src.entities.promotions.Promotion import Promotion

__author__ = 'ezequiel'

class DataLoader:

    @staticmethod
    def loadSampleData():

        sample_data = {}

        # create organization
        o = Organization("ORG0001", "SampleCompany")
        sample_data["org"] = o


        # create some agents
        a1 = Agent("A-001", "Paco", "Martin", "1/1/1990", 200.0, "pmartin@samplecompany.com")
        a2 = Agent("A-002", "Maria", "Fernandez", "10/5/1992", 210.0, "mfernandez@samplecompany.com")
        a3 = Agent("A-003", "JA", "Garcia", "7/12/1989", 210.0, "jag@samplecompany.com")
        o.addAgent(a1)
        o.addAgent(a2)
        o.addAgent(a3)


        # create sample articles
        art1 = Article("123776789087", "Article 1", 12.0, 20.0)
        art2 = Article("003456000082", "Article 2", 10.0, 17.5)
        art3 = Article("783456789085", "Article 3", 1.0, 2.5)
        art4 = Article("993116789000", "Article 4", 35.0, 62.0)


        # create category
        cat1 = Category(001, "CAT1", "Sample Category")
        cat2 = Category(002, "CAT2", "Luxure goods")
        o.addCategory(cat1)
        o.addCategory(cat2)
        cat1.add_articulo(art1)
        cat1.add_articulo(art2)
        cat1.add_articulo(art3)
        cat2.add_articulo(art4)


        # create commissions
        c1 = Commission("Commission 10%", 0.1)
        c2 = Commission("Commission Plus", 0.2)
        commissions = []
        commissions.append(c1)
        commissions.append(c2)

        art2.set_commission(c1)
        art4.set_commission(c1)
        cat2.set_commission(c2)


        # create promotions
        p1=Promotion("Black Friday deals", 0.3, 0.0)
        p2=Promotion("Basic goods", 0.01, 0.0)
        o.addPromotion(p1)
        o.addPromotion(p2)
        p1.addArticle(art4)
        p2.addArticle(art2)



        # create sales
        # agent 1
        sale1 = a1.crearVenta()
        l1 = SaleLine(1, art1)
        l2 = SaleLine(2, art2)
        sale1.add_line(l1)
        sale1.add_line(l2)
        sale1.set_state("pending")

        sale2 = a1.crearVenta()
        l3 = SaleLine(3, art3)
        sale2.add_line(l3)
        sale2.set_state("pending")


        # agent 2
        sale3 = a2.crearVenta()
        l4 = SaleLine(25, art3)
        sale3.add_line(l4)
        sale3.set_state("pending")

        # agent 3

        sale5 = a3.crearVenta()
        l4 = SaleLine(3, art4)
        l5 = SaleLine(1, art2)
        l6 = SaleLine(2,art1)
        sale5.add_line(l4)
        sale5.add_line(l5)
        sale5.add_line(l6)
        sale5.set_state("pending")

        sale6 = a3.crearVenta()
        l7 = SaleLine(8, art3)
        l8 = SaleLine(1, art2)
        sale6.add_line(l7)
        sale6.add_line(l8)
        sale6.set_state("pending")

        return {
                "organization": o,
                "commissions": commissions,
                }
