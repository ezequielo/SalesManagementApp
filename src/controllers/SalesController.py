from src.entities.base.SaleLine import SaleLine
from src.utils.Menus import Menus

__author__ = 'ezequiel'


class SalesController:
    """
    SalesController class allows the application to create, list and remove sales
    given an agent. It also allows to display agent's info
    """

    def __init__(self):
        """
        Init method
        Instantiate an object of the class SalesController

        :return: SalesController object
        """

        pass

    @staticmethod
    def manage_sales(mc, org):
        """
        This is the main controller for managing sales. Its aim is
        to redirect to specific function

        :param mc: MainController
        :param org: Demo Organization
        """

        selected_agent = SalesController.select_agent(mc, org.agent_list)
        while True:
            option = Menus.sales_main_menu()
            if option == 1:
                SalesController.list_sales(selected_agent)
            elif option == 2:
                SalesController.create_sale(selected_agent, org)
            elif option == 3:
                SalesController.remove_sale(selected_agent)
            elif option == 4:
                SalesController.print_summary(selected_agent)
            elif option == 0:
                mc.menu_redirect()

    @staticmethod
    def select_agent(mc, agent_list):
        """
        Helper method for selecting agents given its ID

        :param mc: MainController
        :param agent_list: Agent list
        :return: Chosen agent
        """

        selected_agent = None
        a_id = raw_input("Agent ID: ")
        for agent in agent_list:
            if agent.agent_id == a_id:
                selected_agent = agent
        if selected_agent:
            print("Agent " + selected_agent.agent_id + " selected")
            return selected_agent
        else:
            print("Invalid ID !\n")
            mc.menu_redirect()

    @staticmethod
    def list_sales(agent):
        """
        Prints a list of sales of the current agent

        :param agent: Current selected agent
        """

        print("Sales:\n")
        for sale in agent.sales:
            print(sale)
            print("-" * 30)

    @staticmethod
    def create_sale(agent, org):
        """
        Controller function for creating and adding sales to the current agent's sales list

        :param agent: Selected agent
        :param org: Organization
        """

        lines = []
        menu_back = False
        while not menu_back:
            option = Menus.create_sale_menu()
            if option == 0:
                menu_back = True
            elif option == 1:
                SalesController.add_line(org, lines)
            elif option == 2:
                SalesController.confirm_sale(lines, agent)
                menu_back = True

    @staticmethod
    def add_line(org, lines):
        """
        Helper function whose aim is to creating and adding SaleLines to the current sale

        :param org: Organization
        :param lines: List of lines in the current sale
        """

        selected_article = None
        while selected_article is None:
            art_code = raw_input("Article code: ")
            for category in org.categories:
                for article in category.article_list:
                    if article.ean13 == art_code:
                        selected_article = article
        uds = int(raw_input("Units: "))

        line = SaleLine(uds, selected_article)
        lines.append(line)

    @staticmethod
    def confirm_sale(lines, agent):
        """
        Helper function that adds all lines and generates an invoice.

        :param lines: List of SaleLines
        :param agent: Current selected agent
        """

        if lines:
            sale = agent.create_sale()
            for line in lines:
                sale.add_line(line)
            print("Your sale has been successfully created:\n")
            sale.print_invoice()

    @staticmethod
    def remove_sale(agent):
        """
        This method allows users to delete a sale from the current agent

        :param agent: Current agent
        """

        print("\nSelect a sale to remove:\n")
        i = 1
        for sale in agent.sales:
            print("\t#" + str(i) + " Date: " + str(sale.get_date()) + " - State: " + sale.state + " - Total: "
                  + str(sale.get_total()))
            i += 1
        selection = 0
        while selection < 1 or selection > i:
            selection = int(raw_input("Sale number: "))

        agent.sales.pop(selection - 1)

    @staticmethod
    def print_summary(agent):
        """
        Prints a summary of the current agent, including full name, email, age and salary

        :param agent: Current selected agent
        """

        print("Agent Info\n")
        print("\t Name:\t" + agent.first_name + " " + agent.last_name)
        print("\t Age:\t" + str(agent.get_age()))
        print("\t Email:\t" + agent.email)
        print("\t Base:\t" + str(agent.base))
        print("\t Commissions:\t" + str(agent.get_commissions()))
        print("\t Total:\t" + str(agent.get_total()))
        print("-" * 60)