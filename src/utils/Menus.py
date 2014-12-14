__author__ = 'ezequiel'


class Menus():
    """
    This is a helper class for printing menus and retrieving user's options
    """

    def __init__(self):
        pass

    @staticmethod
    def main_controller_menu():
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

    @staticmethod
    def sales_main_menu():
        """
        Prints sales main menu and asks the user for an option

        :return: User's option
        """

        option = ''
        while option == '':
            print "#"*60 + "\n" + "\t"*4 + "Sales Management\n" + "#"*60
            print "-"*60
            print "1. List sales"
            print "2. Create new sale"
            print "3. Remove sale"
            print "4. Summary"
            print "0. Back"
            print "-"*60
            option = raw_input("Option: ")
            print "-"*60
        return int(option)

    @staticmethod
    def create_sale_menu():
        """
        Displays the operational menu for creating sales

        :return: Agent's option
        """

        print "-"*60
        print "Create new sale"
        print "-"*60
        print "1. Add line"
        print "2. Confirm sale"
        print "0. Back"
        sale_option = raw_input("Option: ")
        print "-"*60
        return int(sale_option)

    @staticmethod
    def org_main_controller():
        """
        Displays the main menu for management options

        :return: User's option
        """

        print "#"*60+"\n"+"\t"*6 + "Organization menu\n" + "#"*60
        print "Select option"
        print "-"*60
        print "1. Manage agents"
        print "2. Manage promotions"
        print "3. Manage categories and articles"
        print "4. Metrics and reports"
        print "0. Back"
        print "-"*60
        option = raw_input("Option: ")
        return int(option)

    @staticmethod
    def org_metrics_menu():
        """
        Displays the metrics menu

        :return: User's option
        """

        print "-"*60
        print "1. Best agent"
        print "2. Quarter balance"
        print "3. Anual balance"
        print "0. Back"
        print "-"*60
        option = raw_input("Select an option: ")
        return int(option)

    @staticmethod
    def agent_menu():
        """
        Displays the agent management menu

        :return: User's option
        """

        print "-"*60
        print "1. List agents"
        print "2. Create new agent"
        print "3. Remove agent"
        print "0. Back"
        print "-"*60
        option = raw_input("Select an option: ")
        return int(option)

    @staticmethod
    def prom_menu():
        """
        Displays the promotion management menu

        :return: User's option
        """

        print "-"*60
        print "1. List promotions"
        print "2. Create new promotion"
        print "3. Remove promotion"
        print "4. Add Article"
        print "5. Remove Article"
        print "0. Back"
        print "-"*60
        option = raw_input("Option : ")
        return int(option)

    @staticmethod
    def art_menu():
        """
        Displays the article management menu

        :return: User's option
        """

        print "-"*60
        print "1. Remove article"
        print "2. Add comission"
        print "3. Remove commission"
        print "0. Back"
        print ""
        option = raw_input("Option: ")
        return int(option)

    @staticmethod
    def subcat_menu():
        """
        Displays subcat main menu

        :return: User's option
        """

        print "-"*60
        print "1. Remove category"
        print "2. Set commission"
        print "3. Remove commission"
        print "4. Create article"
        print "0. Back"
        print "-"*60
        option = raw_input("Option: ")
        return int(option)

    @staticmethod
    def cat_main_menu():
        """
        Displays the categories and articles main menu

        :return: User's option
        """

        print "-"*60
        print "1. List categories"
        print "2. List articles"
        print "3. Create new category"
        print "4. Select category"
        print "5. Select article"
        print "0. Back"
        print "-"*60
        option = raw_input("Select an option: ")
        return int(option)