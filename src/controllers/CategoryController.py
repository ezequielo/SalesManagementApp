from src.entities.base.Category import Category
from src.entities.base.Article import Article
from src.utils.Menus import Menus

__author__ = 'ezequiel'


class CategoryController():
    """
    Category controller
    It's the main controller for every function related to managing categories and articles
    """

    def __init__(self):
        """
        Init function
        Creates and returns an instance of CategoryController

        :return: A CategoryController object
        """
        pass

    @staticmethod
    def cat_controller(org, commissions):
        """
        Cat. controller
        This method represent the controller that will allow the application to manage categories and articles

        :param org: Organization
        :param commissions: List of commissions objects
        """

        menu_back = False
        while not menu_back:
            option = Menus.cat_main_menu()
            if option == 1:
                CategoryController.list_categories(org)
            elif option == 2:
                CategoryController.list_articles(org)
            elif option == 3:
                CategoryController.create_category(org)
            elif option == 4:
                CategoryController.subcat_controller(org, commissions)
            elif option == 5:
                CategoryController.subart_controller(org, commissions)
            elif option == 0:
                menu_back = True

    @staticmethod
    def list_categories(org):
        """
        List categories
        Method responsible of printing all the categories in the organization

        :param org: Organization
        :return:
        """

        for category in org.categories:
            print "-"*30
            print category

    @staticmethod
    def list_articles(org):
        """
        List articles
        Method responsible of printing all the articles in the organization

        :param org: Organization
        """

        for category in org.categories:
            for article in category.list_articulos:
                print article

    @staticmethod
    def create_category(org):
        """
        Create category
        This fuction is able to create a new category and insert it into the organization's categories list

        :param org: Organization
        """

        cat_id = raw_input("Category ID: ")
        cat_name = raw_input("Category name: ")
        cat_desc = raw_input("Category description: ")

        category = Category(cat_id, cat_name, cat_desc)
        org.addCategory(category)

    @staticmethod
    def subcat_controller(org, commissions):
        """
        Subcategory controller
        Responsible of managing all options related to categories

        :param org: Organization
        :param commissions: List of commission objects
        """

        category = CategoryController.select_category(org)
        menu_back = False
        while not menu_back:
            option = Menus.subcat_menu()
            if option == 1:
                CategoryController.remove_category(org, category)
                menu_back = True
            elif option == 2:
                CategoryController.set_commission(category, commissions)
            elif option == 3:
                CategoryController.unset_commission(category)
            elif option == 4:
                CategoryController.create_article(category)
            elif option == 0:
                menu_back = True

    @staticmethod
    def select_category(org):
        """
        Select category
        Allows the user to see a list of the current categories
        and select any category from the previous list

        :param org: Organization
        :return: Category object
        """

        cat_object = None
        i = 1
        for category in org.categories:
            print "-"*30
            print "# " + str(i) + " " + str(category.id_cat) + " %: " + str(category.cat_name)
            i += 1
        selected_cat = 0
        while selected_cat < 1 or selected_cat > i:
            selected_cat = int(raw_input("Select a category: "))
            cat_object = org.categories[selected_cat-1]
        print "Category "+cat_object.cat_name + " selected"
        return cat_object

    @staticmethod
    def remove_category(org, category):
        """
        Remove category
        Method for removing categories from the organization's categories list

        :param org: Organization
        :param category: Category to be removed
        """
        org.categories.remove(category)

    @staticmethod
    def set_commission(category, commissions):
        """
        Set commission
        Given a category and a commission from the list, this
        method allows the app to set commissions into the category

        :param category: Current category
        :param commissions: List of commissions objects
        """

        commission = CategoryController.select_commission(commissions)
        category.set_commission(commission)
        print "The commission has been successfully set"

    @staticmethod
    def unset_commission(category):
        """
        Unset commission
        Allows to unset the commission from the category

        :param category: Current category
        """

        category.set_commission(None)
        print "The commission has been successfully removed"

    @staticmethod
    def create_article(category):
        """
        Create article method
        This method is responsible of creating articles objects and adding
        them into the organization via the current category

        :param category: Current category
        """

        code = raw_input("Code: ")
        name = raw_input("Article name: ")
        cost = float(raw_input("Cost: "))
        listprice = float(raw_input("List price: "))
        article = Article(code, name, cost, listprice)
        category.add_articulo(article)

    @staticmethod
    def subart_controller(org, commissions):
        """
        Sub-article controller
        This is the main controller for everything related to articles.

        :param org: Organization
        :param commissions: List of commission objects
        """

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
        """
        Select article
        Allows the user to select an article. The selected article will be
        the current article until another article is selected

        :param org: Organization
        :return: Current article object
        """

        art = None
        while art is None:
            art_code = raw_input("Article code: ")
            for category in org.categories:
                for article in category.list_articulos:
                    if article.ean13 == art_code:
                        art = article
        print "Article "+art.ean13+" selected."
        return art

    @staticmethod
    def remove_article(org, a):
        """
        Remove article
        This method is able to remove an article from the organization

        :param org: Organization
        :param a: Current article
        """

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
        """
        Select commission
        Displays a list of the available commissions and allows the user to select a commission from the list.

        :param commissions: List of commission objects
        :return: Commission object
        """

        comm_object = None
        i = 1
        for commission in commissions:
            print "# " + str(i) + " " + commission.com_name + " " + str(commission.perc)
            i += 1
        selected_comm2 = 0
        while selected_comm2 < 1 or selected_comm2 > i:
            selected_comm2 = int(raw_input("Select a commission: "))
            comm_object = commissions[selected_comm2-1]
        return comm_object

    @staticmethod
    def add_commission(article, commissions):
        """
        Add commission
        Given an article and a commission objects, this function can add the commission to the article.

        :param article: Current article
        :param commissions: List of commission objects
        """

        commission = CategoryController.select_commission(commissions)
        article.set_commission(commission)
        print "The commission has been successfully set"

    @staticmethod
    def remove_commission(article):
        """
        Remove commission
        This method removes the commission from article

        :param article: Current article
        """
        article.set_commission(None)
        print "The commission has been successfully removed"
