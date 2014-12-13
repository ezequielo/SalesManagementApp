from SalesController import SalesController
from OrgController import OrgController

__author__ = 'ezequiel'


class MainController:

    def __init__(self, dict):
        self.org = dict["organization"]
        self.commissions = dict["commissions"]

    def printMenu(self):
            print "#"*60 + "\n" + "\t"*4 + "Welcome to SalesManagementApp\n" +"#"*60
            print "-"*60
            print "1. Manage Organizations"
            print "2. Agent area"
            print "0. Exit"
            print "-"*60
            option = int(raw_input("Please, select an option: "))
            while option != 1 and option != 2 and option != 0:

                print "\nInvalid option !\n"

                print "-"*60
                print "1. Organization"
                print "2. Sales Management"
                print "0. Exit"
                print "-"*60
                option = int(raw_input("Please, select an option: "))

            if option==1:
                OrgController.printOrg(self, self.org,self.commissions)

            elif option==2:
                SalesController.manageSales(self, self.org)

            elif option==0:
                print "\nBye!\n"