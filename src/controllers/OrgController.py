from src.utils.Menus import Menus
from src.controllers.PromotionController import PromotionController
from src.controllers.CategoryController import CategoryController
from src.controllers.AgentController import AgentController

__author__ = 'ezequiel'


class OrgController:

    def __init__(self):
        pass

    @staticmethod
    def manage_org(mc, org, commissions):

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
        menu_back = False
        while not menu_back:
            option = Menus.org_metrics_menu()
            if option == 1:
                print "The best agent is..."
                print org.best_agent()
            elif option == 2:
                OrgController.quarter_balance(org)
            elif option == 3:
                OrgController.annual_balance(org)
            elif option == 0:
                menu_back = True

    @staticmethod
    def quarter_balance(org):
        quarter = OrgController.get_quarter()
        revenue = org.quarter_balance(quarter)
        print "Total revenue in Q" + str(quarter) + ": " + str(revenue)

    @staticmethod
    def annual_balance(org):
        year = OrgController.get_year()
        revenue = org.anual_balance(year)
        print "Total revenue in " + str(year) + ": " + str(revenue)

    @staticmethod
    def get_quarter():
        quarter = 0
        while quarter > 4 or quarter < 1:
            quarter = int(raw_input("Quarter: "))
        return quarter

    @staticmethod
    def get_year():
        year = 0
        while year < 0:
            year = int(raw_input("Year: "))
        return year