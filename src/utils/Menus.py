__author__ = 'ezequiel'

class Menus():
    """
    This is a helper class for printing menus and retrieving user's options
    """

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
        option = ''
        while option == '':
            print "#"*60 + "\n" + "\t"*4 + "Sales Management\n" +"#"*60
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
        print "#"*60+"\n"+"\t"*6+ "Organization menu\n"+ "#"*60
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