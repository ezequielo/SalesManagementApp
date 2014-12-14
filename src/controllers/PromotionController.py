from src.entities.promotions.Promotion import Promotion
from src.utils.Menus import Menus

__author__ = 'ezequiel'


class PromotionController():
    """
    Class PromotionController
    This class is responsible of all operation related to promotions: Listing, creating and
    deleting of promotions are the common options
    """

    def __init__(self):
        """
        Init method
        Instantiate an object of the class PromotionController

        :return: PromotionController object
        """

        pass

    @staticmethod
    def prom_controller(org):
        """
        Promotion controller method
        This method is responsible of all operation related to promotions

        :param org: Organization
        :return: PromotionController object
        """

        menu_back = False
        while not menu_back:
            option = Menus.prom_menu()
            if option == 1:
                PromotionController.list_promotions(org)
            elif option == 2:
                PromotionController.create_promotion(org)
            elif option == 3:
                PromotionController.remove_promotion(org)
            elif option == 4:
                PromotionController.add_article(org)
            elif option == 5:
                PromotionController.remove_article(org)
            elif option == 0:
                menu_back = True

    @staticmethod
    def list_promotions(org):
        """
        List promotion method
        Responsible of displaying a list of promotions that belong to the organization

        :param org: Organization
        """

        for promotion in org.promotions:
            print("-"*30)
            print(promotion)

    @staticmethod
    def create_promotion(org):
        """
        Create promotion method
        This function aims to create a new promotion and add it to the organization's promotions list

        :param org: Organization
        """

        name = raw_input("Promotion name: ")
        perc = int(raw_input("Promotion percentage: "))
        prom = Promotion(name, perc, 0)
        org.addPromotion(prom)
        print("The promotion " + prom.name + " has been successfully created")

    @staticmethod
    def select_promotion(org):
        """
        Select promotion
        Displays a list of the available promotion and allows the user to select a promotion from the list.

        :param org: Organization
        :return: Promotion object
        """

        i = 1
        for promotion in org.promotions:
            print("-"*30)
            print("# " + str(i) + " " + promotion.name + " %: " + str(promotion.perc))
            i += 1
        selected_prom = 0
        while selected_prom < 1 or selected_prom > i:
            selected_prom = int(raw_input("Select a promotion: "))
        prom_object = org.promotions[selected_prom-1]
        return prom_object

    @staticmethod
    def select_article(org):
        """
        Select article
        Displays a list of the available articles and allows the user to select an article from the list.

        :param org: Organization
        :return: Article object
        """

        selected_article = None
        while selected_article is None:
            art_code = raw_input("Article code: ")
            for category in org.categories:
                for article in category.list_articulos:
                    if article.ean13 == art_code:
                        selected_article = article
        return selected_article

    @staticmethod
    def remove_promotion(org):
        """
        Remove promotion method
        Removes an promotion from the organization's promotion list

        :param org: Organization
        """

        promotion = PromotionController.select_promotion(org)
        org.promotions.remove(promotion)

    @staticmethod
    def add_article(org):
        """
        Add article
        Given an article and a promotion objects, this function can add the article to the promotion.

        :param org: Organization
        """

        promotion = PromotionController.select_promotion(org)
        article = PromotionController.select_article(org)
        promotion.addArticle(article)
        print("Article successfully added")

    @staticmethod
    def remove_article(org):
        """
        Remove article method
        Removes an article from the promotion

        :param org: Organization
        """

        promotion = PromotionController.select_promotion(org)
        article = PromotionController.select_article(org)
        promotion.removeArticle(article)
        print("Article successfully removed")