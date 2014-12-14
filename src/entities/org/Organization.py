__author__ = 'ezequiel'


class Organization():
    """

    Organization class
    This class aim to models the organization objects and it also acts like an container of the organization's info
    such as list of agents, promotions, categories, etc.

    """
    def __init__(self, cif, org_name):
        """

        Init method
        Creates a new instance of Organization

        :param cif: Organization's ID
        :param org_name: Organization's name
        :return: Organization object

        """
        self.cif = cif
        self.org_name = org_name
        self.agent_list = []
        self.promotions = []
        self.categories = []

    # Getters and setters
    def get_agent_list(self):
        """

        Get agent list
        Return a list of agent who work at the organization

        :return: List of Agent objects

        """
        return self.agent_list

    def set_agents(self, agent_list):
        """

        Set agents
        Allows to replace the agents list of an organization with a new given list

        :param agent_list: Agent list

        """
        self.agent_list = agent_list

    def get_promotions(self):
        """

        Get promotions list
        Return a list of promotions of the organization

        :return: List of Promotions objects

        """
        return self.promotions

    def set_promotions(self, promotions):
        """
        Set promotions
        Allows to replace the promotions list of an organization with a new given list

        :param promotions: Promotions list

        """
        self.promotions = promotions

    def get_categories(self):
        """

        Get categories list
        Return a list of categories of the organization

        :return: List of Categories objects

        """
        return self.categories

    def set_categories(self, categories):
        """

        Set categories
        Allows to replace the categories list of an organization with a new given list

        :param categories: Categories list

        """
        self.categories = categories

    def get_org_name(self):
        """

        Get organization name
        Returns an string containing the organization name of the organization object that calls the method

        :return: Organization name

        """
        return self.org_name

    def set_org_name(self, org_name):
        """

        Set organization name
        Setter method that allows changing the organization name with for a give new name

        :param org_name: New name

        """
        self.org_name = org_name

    def get_cif(self):
        """

        Get CIF
        This method will return the organization ID

        :return: Organization ID

        """
        return self.cif

    def set_cif(self, cif):
        """

        Set CIF
        This method allows changing the organization CIF given a new ID

        :param cif: New organization ID

        """
        self.cif = cif

    def __str__(self):
        """

        String method
        This method allows printing Organization objects in a easier way

        :return: String containing organization info

        """
        return self.org_name + " CIF:" + self.cif

    # Main methods
    def add_agent(self, agent):
        """

        Add agent method
        Allows to add a new agent to the organization agents list

        :param agent: Agent object
        """
        agent.set_org(self)
        self.agent_list.append(agent)

    def remove_agent(self, agent):
        """

        Remove agent method
        This method aims to remove a given agent from the organization agent list

        :param agent: Agent to be removed

        """
        agent.set_org(None)
        self.agent_list.remove(agent)

    def add_category(self, category):
        """

        Add category method
        Allows to add a new category to the organization agents list

        :param category: Category object

        """
        category.set_org(self)
        self.categories.append(category)

    def remove_category(self, category):
        """

        Remove category method
        This method aims to remove a given category from the organization category list

        :param category: Category to be removed

        """
        category.set_org(None)
        self.categories.remove(category)

    def add_promotion(self, promotion):
        """

        Add promotion method
        Allows to add a new promotion to the organization agents list

        :param promotion: Promotion object

        """
        promotion.set_org(self)
        self.promotions.append(promotion)

    def remove_promotions(self, promotion):
        """

        Remove promotion method
        This method aims to remove a given promotion from the organization promotions list

        :param promotion: Promotion to be removed

        """
        promotion.set_org(None)
        self.promotions.remove(promotion)

    def best_agent(self):
        """

        Best agent
        This method evaluates the agents who work at the organization an
        returns the best on according to the sales results

        :return: Agent object

        """
        num_max = 0.0
        best_agent = None
        for agent in self.agent_list:
            if agent.get_total() > num_max:
                num_max = agent.get_total()
                best_agent = agent
        return best_agent

    def annual_balance(self, year):
        """

        Annual balance
        Given a year, this method can return the total revenue of the year

        :param year: Year to be evaluated
        :return: Total revenue

        """
        total_cost = 0.0
        total_sold = 0.0
        total_comm = 0.0
        for agent in self.agent_list:
            # commissions
            total_comm = total_comm + agent.get_commissions()
            # cost and sold
            cost_sale = 0.0
            sold_sale = 0.0
            sold_line = 0.0
            cost_line = 0.0
            for sale in agent.sales:
                if sale.get_date().year == year:
                    sold_line = 0.0
                    cost_line = 0.0
                    for line in sale.lines:
                        sold_line = sold_line + line.get_subtotal()
                        cost_line = cost_line + line.get_uds() * line.art.get_cost()
                sold_sale = total_sold + sold_line
                cost_sale = total_cost + cost_line
            total_cost += cost_sale
            total_sold += sold_sale
        total_revenue = total_sold - total_cost - total_comm
        return total_revenue

    def quarter_balance(self, year, quarter):
        """

        Quarter balance
        Given a quarter, this method can return the total revenue of the the quarter

        :param quarter: Quarter to be evaluated
        :return: Total revenue in the quarter

        """
        if quarter == 1:
            month_list = [1, 2, 3]
        elif quarter == 2:
            month_list = [4, 5, 6]
        elif quarter == 3:
            month_list = [7, 8, 9]
        else:
            month_list = [10, 11, 12]
        total_cost = 0.0
        total_sold = 0.0
        total_comm = 0.0
        for agent in self.agent_list:
            # commissions
            total_comm = total_comm + agent.get_commissions()
            # cost and sold
            cost_sale = 0.0
            sold_sale = 0.0
            for sale in agent.sales:
                sold_line = 0.0
                cost_line = 0.0
                if sale.get_date().year == year and sale.get_date().month in month_list:
                    for line in sale.lines:
                        sold_line = sold_line + line.get_subtotal()
                        cost_line = cost_line + line.get_uds() * line.art.get_cost()
                sold_sale = total_sold + sold_line
                cost_sale = total_cost + cost_line
            total_cost += cost_sale
            total_sold += sold_sale
        total_revenue = total_sold - total_cost - total_comm
        return total_revenue