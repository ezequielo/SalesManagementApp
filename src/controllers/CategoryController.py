from src.entities.base.Category import Category
from src.entities.base.Article import Article
from src.utils.Menus import Menus

__author__ = 'ezequiel'

class CategoryController():

    @staticmethod
    def cat_controller(org, commissions):
        menu_back = False
        while menu_back == False:
            option = Menus.cat_main_menu()
            if option == 1:
                CategoryController.list_categories(org)
            elif option == 2:
                CategoryController.list_articles(org)
            elif option == 3:
                CategoryController.create_category(org)
            elif option ==4:
                CategoryController.subcat_controller(org, commissions)
            elif option ==5:
                CategoryController.subart_controller(org, commissions)
            elif option ==0:
                menu_back = True


    @staticmethod
    def list_categories(org):
        for category in org.categories:
            print "-"*30
            print category

    @staticmethod
    def list_articles(org):
        for category in org.categories:
            for article in category.list_articulos:
                print article

    @staticmethod
    def create_category(org):
        cat_id = raw_input("Category ID: ")
        cat_name =raw_input("Category name: ")
        cat_desc=raw_input("Category description: ")

        category = Category(cat_id,cat_name,cat_desc)
        org.addCategory(category)


    @staticmethod
    def subcat_controller(org, commissions):

        category = CategoryController.select_category()

        menu_back = False
        while not menu_back:
            option = Menus.subcat_menu()
            if option == 1:
                CategoryController.remove_category(org, category)
                menu_back = True
            elif option == 2:
                CategoryController.set_commission(category, commissions)
            elif option ==3:
                CategoryController.unset_commission(category)
            elif option ==4:
                CategoryController.create_article(category)
            elif option==0:
                menu_back=True


    @staticmethod
    def select_category(org):
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
        return cat_object

    @staticmethod
    def remove_category(org, category):
        org.categories.remove(category)

    @staticmethod
    def set_commission(category, commissions):
        commission = CategoryController.select_commission(commissions)
        category.set_commission(commission)
        print "The commission has been successfully set"


    @staticmethod
    def unset_commission(category):
        category.set_commission(None)
        print "The commission has been successfully removed"

    @staticmethod
    def create_article(category):
        code = raw_input("Code: ")
        name = raw_input("Article name: ")
        cost =float(raw_input("Cost: "))
        listprice = float(raw_input("List price: "))
        article = Article(code, name, cost, listprice)
        category.add_articulo(article)



    @staticmethod
    def subart_controller(org, commissions):
        selected_article = CategoryController.select_article(org)
        menu_back = False
        while not menu_back:
            option = Menus.art_menu()
            if option == 1:
                CategoryController.remove_article(org, selected_article)
                menu_back = True
            elif option == 2:
                CategoryController.add_commission(selected_article, commissions)
            elif option == 3:
                CategoryController.remove_commission(selected_article)
            elif option == 0:
                menu_back = True

    @staticmethod
    def select_article(org):
        art = None
        while art == None:
            art_code = raw_input("Article code: ")
            for category in org.categories:
                for article in category.list_articulos:
                    if article.ean13 == art_code:
                        art = article
        print "Article "+art.ean13+" selected."
        return art

    @staticmethod
    def remove_article(org, a):
        remove = False
        for category in org.categories:
            for article in category.list_articulos:
                if article == a:
                    remove = True
            if remove:
                category.remove_articulo(a)
        print "The article has been successfully removed"

    @staticmethod
    def select_commission(commissions):
        i = 1
        for commission in commissions:
            print "# " +str(i) + " "+commission.com_name + " "+str(commission.perc)
            i = i +1
        selected_comm2 = 0
        while selected_comm2 <1 or selected_comm2 > i:
            selected_comm2 = int(raw_input("Select a commission: "))
            comm_object = commissions[selected_comm2-1]
        return comm_object


    @staticmethod
    def add_commission(article, commissions):
        commission = CategoryController.select_commission(commissions)
        article.set_commission(commission)
        print "The commission has been successfully set"

    @staticmethod
    def remove_commission(article):
        article.set_commission(None)
        print "The commission has been successfully removed"
