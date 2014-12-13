__author__ = 'ezequiel'
import datetime

class Organization():

    # Constructor

    def __init__(self, cif, org_name):
        self.cif = cif
        self.org_name=org_name
        self.agent_list = []
        self.promotions = []
        self.categories = []

    # Getters and setters

    def get_agent_list(self):
        return self.agent_list

    def set_agents(self, agent_list):
        self.agents = agent_list

    def get_promotions(self):
        return self.promotions

    def set_promotions(self, promotions):
        self.promotions = promotions

    def get_categories(self):
        return self.categories

    def set_categories(self, categories):
        self.categories = categories

    def get_org_name(self, org_name):
        return org_name

    def set_org_name(self, org_name):
        self.org_name=org_name

    def get_cif(self):
        return self.cif

    def set_cif(self,cif):
        self.cif =cif

    def __str__(self):
     return self.org_name+ " CIF:" +self.cif

    # Main methods

    def addAgent(self, agent):
        agent.set_org(self)
        self.agent_list.append(agent)


    def removeAgent(self, agent):
        agent.set_org(None)
        self.agent_list.remove(agent)

    def addCategory(self, category):
        category.set_org(self)
        self.categories.append(category)

    def removeCategory(self, category):
        category.set_org(None)
        self.categories.remove(category)

    def addPromotion(self, promotion):
        promotion.set_org(self)
        self.promotions.append(promotion)

    def removePromotions(self, promotion):
        promotion.set_org(None)
        self.promotions.remove(promotion)


    def best_agent(self):
        max = 0.0
        best_agent = None
        for agent in self.agent_list:
            if agent.getTotal() > max:
                max = agent.getTotal()
                best_agent = agent
        return best_agent


    def anual_balance(self,year):
        total_cost = 0.0
        total_sold = 0.0
        total_comm = 0.0
        total_revenue = 0.0

        for agent in self.agent_list:
            # comisiones
            total_comm = total_comm + agent.getComisiones()

            # cost and sold
            cost_sale = 0.0
            sold_sale = 0.0
            for sale in agent.sales:
                if sale.get_date().year == year:
                    sold_line = 0.0
                    cost_line = 0.0
                    for line in sale.lines:
                        sold_line = sold_line + line.getSubtotal()
                        cost_line = cost_line + line.get_uds() * line.art.get_cost()

                sold_sale=total_sold+sold_line
                cost_sale=total_cost+cost_line

            total_cost=total_cost+cost_sale
            total_sold=total_sold+sold_sale


        total_revenue=total_sold-total_cost-total_comm
        return total_revenue



    def quarter_balance(self,quarter):

        if quarter == 1:
            month_list = [1,2,3]
        elif quarter == 2:
            month_list = [4,5,6]
        elif quarter == 3:
            month_list = [7,8,9]
        else:
            month_list = [10,11,12]

        total_cost = 0.0
        total_sold = 0.0
        total_comm = 0.0

        for agent in self.agent_list:
            # comisiones
            total_comm = total_comm + agent.getComisiones()

            # cost and sold
            cost_sale = 0.0
            sold_sale = 0.0
            for sale in agent.sales:
                sold_line = 0.0
                cost_line = 0.0
                if sale.get_date().year == datetime.datetime.today().year and sale.get_date().month in month_list:
                    for line in sale.lines:
                        sold_line = sold_line + line.getSubtotal()
                        cost_line = cost_line + line.get_uds() * line.art.get_cost()

                sold_sale=total_sold+sold_line
                cost_sale=total_cost+cost_line

            total_cost=total_cost+cost_sale
            total_sold=total_sold+sold_sale


        total_revenue=total_sold-total_cost-total_comm
        return total_revenue