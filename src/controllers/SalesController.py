from src.entities.base.SaleLine import SaleLine

__author__ = 'ezequiel'


class SalesController:
    @staticmethod
    def manage_sales(mc, org):
        ok = False
        while ok == False:
            selected_agent = None
            print "-" * 60
            id_agent = raw_input("Agent ID: ")
            for agent in org.agent_list:
                if agent.agent_id == id_agent:
                    selected_agent = agent
            if selected_agent:
                print "Agent " + selected_agent.agent_id + " selected"
                ok2 = False
                while ok2 == False:
                    print "#" * 60 + "\n" + "\t" * 4 + "Sales Management\n" + "#" * 60
                    print "-" * 60
                    print "1. List sales"
                    print "2. Create new sale"
                    print "3. Remove sale"
                    print "4. Summary"
                    print "0. Back"
                    print "-" * 60
                    option = int(raw_input("Option: "))
                    print "-" * 60
                    if option == 1:
                        print "Sales:\n"
                        for sale in selected_agent.sales:
                            print sale
                            print "-" * 30
                    elif option == 2:
                        lines = []
                        exits = False
                        while exits == False:
                            print "-" * 60
                            print "Create new sale"
                            print "-" * 60
                            print "1. Add line"
                            print "2. Confirm sale"
                            print "0. Back"
                            sale_option = int(raw_input("Option: "))
                            print "-" * 60
                            if sale_option == 0:
                                exits = True
                            elif sale_option == 1:
                                selected_article = None
                                while selected_article == None:
                                    art_code = raw_input("Article code: ")
                                    for category in org.categories:
                                        for article in category.list_articulos:
                                            if article.ean13 == art_code:
                                                selected_article = article
                                uds = int(raw_input("Units: "))
                                line = SaleLine(uds, selected_article)
                                lines.append(line)
                            elif sale_option == 2:
                                if lines:
                                    sale = selected_agent.create_sale()
                                    for line in lines:
                                        sale.add_line(line)
                                    print "Your sale has been successfully created:\n"
                                    sale.print_invoice()
                                    exits = True
                    elif option == 3:
                        print "\nSelect a sale to remove:\n"
                        i = 1
                        for sale in selected_agent.sales:
                            print "\t#" + str(i) + " Date: " + str(sale.get_date()) + " - State: " + sale.state + " - Total: " + str(sale.get_total())
                            i = i + 1
                        selection = 0
                        while selection < 1 or selection > i:
                            selection = int(raw_input("Sale number: "))
                        selected_agent.sales.pop(selection - 1)
                    elif option == 4:
                        print "Agent Info\n"
                        print "\t Name:\t" + selected_agent.first_name + " " + selected_agent.last_name
                        print "\t Age:\t" + str(selected_agent.get_age())
                        print "\t Email:\t" + selected_agent.email
                        print "\t Base:\t" + str(selected_agent.base)
                        print "\t Commissions:\t" + str(selected_agent.get_commissions())
                        print "\t Total:\t" + str(selected_agent.get_total())
                        print "-" * 60
                    elif option == 0:
                        mc.print_menu()
            else:
                print "Invalid ID"