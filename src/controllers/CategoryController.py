__author__ = 'ezequiel'

class CategoryController():

    @staticmethod
    def cat_controller(org, commissions):

        menu_back = False
        while menu_back == False:
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
                menu_back = True