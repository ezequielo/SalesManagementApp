from src.utils.Menus import Menus
from src.controllers.PromotionController import PromotionController
from src.controllers.CategoryController import CategoryController
from src.controllers.AgentController import AgentController

__author__ = 'ezequiel'


class OrgController:
    """
    Class OrgController
    This class is responsible of the management area. Listing, creating and
    deleting of every model are the common options
    """

    def __init__(self):
        """
        Init method
        Instantiate an object of the class OrgController

        :return: OrgController object
        """

        pass

    @staticmethod
    def manage_org(mc, org, commissions):
        """
        Manage organization function
        This is the method that does the actual work when it comes to manage the organization.

        :param mc: MainController instance
        :param org: Organization
        :param commissions: List of commission objects
        """

        menu_back = False
        while not menu_back:
            option = Menus.org_main_controller()
            if option == 1:
                AgentController.agent_controller(org)
            elif option == 2:
                PromotionController.prom_controller(org)
            elif option == 3:
                CategoryController.cat_controller(org, commissions)
            elif option == 4:
                OrgController.metrics_controller(org)
            elif option == 0:
                mc.menu_redirect()

    @staticmethod
    def metrics_controller(org):
        """
        Metrics controller
        Allows the user to choose any from the available metrics and call the right methods to generate them

        :param org: Organization
        """

        menu_back = False
        while not menu_back:
            option = Menus.org_metrics_menu()
            if option == 1:
                print("The best agent is...")
                print(org.best_agent())
            elif option == 2:
                OrgController.quarter_balance(org)
            elif option == 3:
                OrgController.annual_balance(org)
            elif option == 0:
                menu_back = True

    @staticmethod
    def quarter_balance(org):
        """
        Quarter balance
        Displays balance information about the given quarter.

        :param org: Organization
        """

        quarter = OrgController.get_quarter()
        revenue = org.quarter_balance(quarter)
        print("Total revenue in Q" + str(quarter) + ": " + str(revenue))

    @staticmethod
    def annual_balance(org):
        """
        Annual balance
        Displays balance information about the given year.

        :param org: Organization
        """

        year = OrgController.get_year()
        revenue = org.anual_balance(year)
        print("Total revenue in " + str(year) + ": " + str(revenue))

    @staticmethod
    def get_quarter():
        """
        Allows the user to input the quarter they want to see

        :return: Integer representing the quarter
        """

        quarter = 0
        while quarter > 4 or quarter < 1:
            quarter = int(raw_input("Quarter: "))
        return quarter

    @staticmethod
    def get_year():
        """
        Allows the user to insert the year of the annual balance

        :return: Year
        """

        year = 0
        while year < 0:
            year = int(raw_input("Year: "))
        return year