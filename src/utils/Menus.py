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
