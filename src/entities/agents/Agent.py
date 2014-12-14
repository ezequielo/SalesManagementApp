__author__ = 'ezequiel'

from datetime import date
from src.entities.base.Sale import Sale


class Agent:
    """

    Agent class
    This class is responsible of modeling commercial agents

    """
    def __init__(self, agent_id, first_name, last_name, birth_date, base, email):
        """

        Init method
        Initialize an Agent object given the following parameters

        :param agent_id: Agent ID
        :param first_name: First name
        :param last_name: Last name
        :param birth_date: Birth date
        :param base: Base salary
        :param email: E-mail

        """
        self.agent_id = agent_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.base = base
        self.email = email
        self.sales = []
        self.org = None

    # Getter and setters
    def get_sales(self):
        """

        Get sales method
        Returns a list of the sales made by the agent that calls the method

        :return: List of sales

        """
        return self.sales

    def get_name(self):
        """

        Get name method
        Returns the agent's full name

        :return: Agent's full name

        """
        return self.last_name + ', ' + self.first_name

    def get_agent_id(self):
        """

        Get agent ID
        Return the current agent's ID

        :return: Agent's ID

        """
        return self.agent_id

    def get_age(self):
        """

        Get age method
        Returns the current agent's age

        :return: Agent's age

        """
        today = date.today()
        l = self.birth_date.split("/")
        f_bir = date(int(l[2]), int(l[1]), int(l[0]))
        years = ((today.year - f_bir.year - 1) +
                (1 if (today.month, today.day) >= (f_bir.month, f_bir.day) else 0))
        return years

    def get_birth_date(self):
        """

        Get birth_date
        Getter method that returns agent's birth date

        :return: Agent's birth date

        """
        return self.birth_date

    def set_birth_date(self, birth_date):
        """

        Set birth_date
        Setter method that can set the agent's birth date.

        :param birth_date: Birth date

        """
        self.birth_date = birth_date

    def set_agent_id(self, new_id):
        """

        Set agent ID
        Setter for agent's ID attribute

        :param new_id: New ID to be set

        """
        self.agent_id = new_id

    def get_base(self):
        """

        Get base
        Returns the agent's base salary

        :return: Agent's base salary

        """
        return self.base

    def set_base(self, base):
        """
        Set base method
        Allows to set the base salary of a given agent

        :param base: Base salary
        """
        self.base = base

    def get_email(self):
        """

        Get email
        Returns the email of the agent who calls the method

        :return: Agent's email

        """
        return self.email

    def set_email(self, email):
        """

        Set email
        This method can replace the email attribute for the given one as a parameter

        :param email: New email

        """
        self.email = email

    def get_org(self):
        """

        Get organization
        Returns the organization the agent belongs

        :return: Organization object

        """
        return self.org

    def set_org(self, org):
        """

        Set organization method
        Allows to set the organization of an given agent

        :param org: Organization

        """
        self.org = org

    def __str__(self):
        """

        String method
        Allows to print objects in a natural way

        :return: String containing agent's info

        """
        return self.first_name + " " + self.last_name + " - " + self.email

    # Main methods
    def get_commissions(self):
        """

        Get commissions
        Given an agent and all the sales they have done, this method can return the commissions earned by the agent

        :return: Value representing total earned in commissions

        """
        commissions = 0.0
        comm_percentage = 0
        for sale in self.sales:
            for line in sale.lines:
                article = line.get_art()
                if article.get_commission():
                    comm_percentage = article.commission.get_percentage()
                else:
                    cat_list = self.org.get_categories()
                    for category in cat_list:
                            for art in category.get_article_list():
                                if art.get_ean13() == article.get_ean13():
                                    if category.get_commission():
                                        commissions = category.get_commission()
                                        comm_percentage = commissions.get_percentage()
                                else:
                                    comm_percentage = 0.0
                comm_art = article.get_list_price() * comm_percentage
                comm_line = comm_art * line.get_uds()
                commissions += comm_line
        return commissions

    def get_total(self):
        """

        Get total allows the agent to get its salary based on the commissions earned and the salary base

        :return: Value representing the total salary

        """
        commissions = 0.0
        comm_percentage = 0.0
        article = None
        line = None
        for sale in self.sales:
            for line in sale.get_lines():
                article = line.get_art()
                if article.get_commission():
                    comm_percentage = article.commission.get_percentage()
                else:
                    cat_list = self.org.get_categories()
                    for category in cat_list:
                        for art in category.get_article_list():
                            if art.get_ean13() == article.get_ean13():
                                if category.get_commission():
                                    comm_percentage = category.commission.get_percentage()
                            else:
                                comm_percentage = 0.0
            comm_art = article.get_list_price() * comm_percentage
            comm_line = comm_art * line.get_uds()
            commissions += comm_line
        total = self.base + commissions
        return total

    def create_sale(self):
        """

        Create sale

        Allows the agent to generate a new sale and add it to its sales list
        :return: Sale object

        """
        v = Sale()
        self.sales.append(v)
        return v