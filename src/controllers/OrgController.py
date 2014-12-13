from datetime import datetime
from src.entities.org.Organization import Organization
from src.entities.agents.Agent import Agent
from src.entities.base.Category import Category
from src.entities.promotions.Promotion import Promotion
from src.entities.base.Article import Article
from src.entities.agents.Commission import Commission

__author__ = 'ezequiel'

class OrgController:

    @staticmethod
    def printOrg(mc, org, commissions):

        org_exit = False
        while org_exit == False:

            print "#"*60+"\n"+"\t"*6+ "Organization menu\n"+ "#"*60
            print "Select option"
            print "-"*60
            print "1. Manage agents"
            print "2. Manage promotions"
            print "3. Manage categories and articles"
            print "4. Metrics and reports"
            print "0. Back"
            print "-"*60
            option = int(raw_input("Option: "))



            if option == 1:
                exit = False
                while exit == False:
                    print "-"*60
                    print "1. List agents"
                    print "2. Create new agent"
                    print "3. Remove agent"
                    print "0. Back"
                    print "-"*60
                    agent_ops = int(raw_input("Select an option: "))

                    if agent_ops == 1:
                        for agent in org.agent_list:
                            print "-"*30
                            print agent
                    elif agent_ops == 2:
                        id = raw_input("Agent ID: ")
                        firstname = raw_input("First name: ")
                        lastname = raw_input("Last name: ")
                        birthdate = raw_input("Birth date name: ")
                        email = raw_input("e-Mail: ")
                        base = float(raw_input("Base: "))

                        a = Agent(id, firstname, lastname, birthdate, base, email)
                        org.addAgent(a)
                        print "The agent with ID " + a.agent_id + "has been successfully created and added to the company"


                    elif agent_ops == 3:
                        i =1
                        for agent in org.agent_list:
                            print "-"*30
                            print "#"+str(i) + " - First name: "+agent.firstname+" Last name" + agent.lastname + " ID: "+agent.agent_id
                            i = i +1

                        selection = 0
                        while selection <1 or selection > i:
                            selection = int(raw_input("Select the agent to be deleted: "))

                        org.agent_list.pop(selection-1)

                    elif agent_ops == 0:
                        exit = True


            elif option == 2:

                exit_promotions = False
                while exit_promotions == False:
                    print "-"*60
                    print "1. List promotions"
                    print "2. Create new promotion"
                    print "3. Remove promotion"
                    print "4. Add Article"
                    print "5. Remove Article"
                    print "0. Back"
                    print "-"*60
                    prom_op = int(raw_input("Option : "))

                    if prom_op == 1:
                        for promotion in org.promotions:
                            print "-"*30
                            print promotion

                    elif prom_op == 2:
                        name = raw_input("Promotion name: ")
                        perc = int(raw_input("Promotion percentage: "))
                        prom = Promotion(name, perc, 0)
                        org.addPromotion(prom)
                        print "The promotion " +prom.name+ " has been successfully created"

                    elif prom_op == 3:
                        i = 1
                        for promotion in org.promotions:
                            print "-"*30
                            print "# " +str(i) +" "+ promotion.name + " %: "+ str(promotion.perc)
                            i = i+1

                        selected_prom = 0
                        while selected_prom <1 or selected_prom > i:
                            selected_prom = int(raw_input("Select a promotion to remove: "))

                        org.promotions.pop(selected_prom-1)

                    elif prom_op == 4:

                        i = 1
                        for promotion in org.promotions:
                            print "-"*30
                            print "# " +str(i) +" "+ promotion.name + " %: "+ str(promotion.perc)
                            i = i+1

                        selected_prom = 0
                        while selected_prom <1 or selected_prom > i:
                            selected_prom = int(raw_input("Select a promotion: "))

                        prom_object = org.promotions[selected_prom-1]

                        selected_article = None
                        while selected_article == None:
                            art_code = raw_input("Article code: ")
                            for category in org.categories:
                                for article in category.list_articulos:
                                    if article.ean13 == art_code:
                                        selected_article = article

                        prom_object.addArticle(selected_article)
                        print "Article successfully added"

                    elif prom_op == 5:
                        i = 1
                        for promotion in org.promotions:
                            print "-"*30
                            print "# " +str(i) +" "+ promotion.name + " %: "+ str(promotion.perc)
                            i = i+1


                        selected_prom = 0
                        while selected_prom <1 or selected_prom > i:
                            selected_prom = int(raw_input("Select a promotion: "))

                        prom_object = org.promotions[selected_prom-1]

                        selected_article = None
                        while selected_article == None:
                            art_code = raw_input("Article code: ")
                            for category in org.categories:
                                for article in category.list_articulos:
                                    if article.ean13 == art_code:
                                        selected_article = article

                        prom_object.removeArticle(selected_article)
                        print "Article successfully removed"

                    elif prom_op == 0:
                        exit_promotions = True

            elif option == 3:

                exit_categories = False
                while exit_categories == False:
                    print "-"*60
                    print "1. List categories"
                    print "2. List articles"
                    print "3. Create new category"
                    print "4. Select category"
                    print "5. Select article"
                    print "0. Back"
                    print "-"*60
                    cat_ops = int(raw_input("Select an option: "))

                    if cat_ops == 1:
                        for category in org.categories:
                            print "-"*30
                            print category

                    elif cat_ops == 2:
                        for category in org.categories:
                            for article in category.list_articulos:
                                print article

                    elif cat_ops == 3:
                        cat_id = raw_input("Category ID: ")
                        cat_name =raw_input("Category name: ")
                        cat_desc=raw_input("Category description: ")

                        category = Category(cat_id,cat_name,cat_desc)
                        org.addCategory(category)

                    elif cat_ops ==4:

                        i = 1
                        for category in org.categories:
                            print "-"*30
                            print "# " +str(i) +" "+ str(category.id_cat)+ " %: "+ str(category.cat_name)
                            i = i+1
                        selected_cat = 0
                        while selected_cat <1 or selected_cat > i:
                            selected_cat = int(raw_input("Select a category: "))
                            cat_object = org.categories[selected_cat-1]

                        print "Category "+cat_object.cat_name +" selected"

                        exit_cat2 = False
                        while exit_cat2 == False:
                            print "-"*60
                            print "1. Remove category"
                            print "2. Set commission"
                            print "3. Remove commission"
                            print "4. Create article"
                            print "0. Back"
                            print "-"*60
                            cat2_option = int(raw_input("Option: "))

                            if cat2_option == 1:
                                org.categories.pop(selected_cat-1)
                                exit_cat2 = True

                            elif cat2_option == 2:

                                i = 1
                                for commission in commissions:
                                    print "# " +str(i) + " "+commission.com_name + " "+str(commission.perc)
                                    i = i +1
                                selected_comm = 0
                                while selected_comm <1 or selected_comm > i:
                                    selected_comm = int(raw_input("Select a commission: "))
                                    comm_object = commissions[selected_comm-1]

                                cat_object.set_commission(comm_object)
                                print "The commission has been successfully set"

                            elif cat2_option ==3:
                                cat_object.set_commission(None)
                                print "The commission has been successfully removed"

                            elif cat2_option ==4:
                                code = raw_input("Code: ")
                                name = raw_input("Article name: ")
                                cost =float(raw_input("Cost: "))
                                listprice = float(raw_input("List price: "))

                                article = Article(code, name, cost, listprice)
                                cat_object.add_articulo(article)

                            elif cat2_option==0:
                                exit_cat2=True



                    elif cat_ops ==5:
                        selected_article = None
                        while selected_article == None:
                            art_code = raw_input("Article code: ")
                            for category in org.categories:
                                for article in category.list_articulos:
                                    if article.ean13 == art_code:
                                        selected_article = article

                        print "Article "+selected_article.ean13+" selected."

                        exit_article =False
                        while exit_article == False:
                            print "-"*60
                            print "1. Remove article"
                            print "2. Add comission"
                            print "3. Remove commission"
                            print "0. Back"
                            print ""

                            art_opt= int(raw_input("Option: "))

                            if art_opt == 1:
                                remove = False
                                for category in org.categories:

                                    for article in category.list_articulos:
                                        if article == selected_article:
                                            remove = True
                                    if remove == True:
                                        category.remove_articulo(selected_article)
                                print "The article has been successfully removed"
                                exit_article = True

                            elif art_opt == 2:

                                i = 1
                                for commission in commissions:
                                    print "# " +str(i) + " "+commission.com_name + " "+str(commission.perc)
                                    i = i +1
                                selected_comm2 = 0
                                while selected_comm2 <1 or selected_comm2 > i:
                                    selected_comm2 = int(raw_input("Select a commission: "))
                                    comm_object = commissions[selected_comm2-1]

                                selected_article.set_commission(comm_object)

                                print "The commission has been successfully set"

                            elif art_opt == 3:
                                selected_article.set_commission(None)
                                print "The commission has been successfully removed"

                            elif art_opt == 0:
                                exit_article = True


                    elif cat_ops ==0:
                        exit_categories = True

            elif option == 4:
                exit_metrics = False
                while exit_metrics == False:

                    print "-"*60
                    print "1. Best agent"
                    print "2. Quarter balance"
                    print "3. Anual balance"
                    print "0. Back"
                    print "-"*60
                    metrics_ops = int(raw_input("Select an option: "))

                    if metrics_ops == 1:
                        print "The best agent in the company is..."
                        print org.best_agent()
                    elif metrics_ops == 2:
                        quarter = 0
                        while quarter >4 or quarter<1:
                            quarter = int(raw_input("Quarter: "))

                        revenue=org.quarter_balance(quarter)
                        print "Total revenue in Q" +str(quarter) +": " +str(revenue)

                    elif metrics_ops == 3:
                        year = 0
                        while year == 0:
                            year = int(raw_input("Year: "))

                        revenue = org.anual_balance(year)
                        print "Total revenue in " +str(year) +": " +str(revenue)
                    elif metrics_ops == 0:
                        exit_metrics = True


            elif option == 0:
                mc.printMenu()

