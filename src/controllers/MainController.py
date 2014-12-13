__author__ = 'ezequiel'

from src.controllers.SalesController import SalesController
from src.controllers.OrgController import OrgController


class MainController:
    """
    MainController is the class that models the
    controller for the terminal-based interface.
    """
    def __init__(self, sample_data):
        """
        Init method for MainController
        :param sample_data: Dictionary with the organization's data
        :return: A MainController instance
        """
        self.org = sample_data["organization"]
        self.commissions = sample_data["commissions"]

    def get_option(self):
        """
        Prints main menu and asks the user for an option
        :return: User's option
        """
        option = None
        while option != 1 and option != 2 and option != 0:
            print("-"*60)
            print("\t\tSalesManagementApp")
            print("-"*60)
            print("1. Organization")
            print("2. Sales Management")
            print("0. Exit")
            print("-"*60)
            option = int(raw_input("Please, select an option: "))
        return option

    def menu_redirect(self):
        """
        Redirect the user to another menu depending on their option
        :return: Void
        """
        option = self.get_option()
        if option == 1:
            OrgController.printOrg(self, self.org, self.commissions)
        elif option == 2:
            SalesController.manageSales(self, self.org)
        elif option == 0:
            print "\nBye!\n"
