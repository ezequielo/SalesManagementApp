from src.entities.promotions.Promotion import Promotion
from src.utils.Menus import Menus

__author__ = 'ezequiel'


class PromotionController():

    def __init__(self):
        pass

    @staticmethod
    def prom_controller(org):
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
        for promotion in org.promotions:
            print "-"*30
            print promotion

    @staticmethod
    def create_promotion(org):
        name = raw_input("Promotion name: ")
        perc = int(raw_input("Promotion percentage: "))
        prom = Promotion(name, perc, 0)
        org.addPromotion(prom)
        print "The promotion " + prom.name + " has been successfully created"

    @staticmethod
    def select_promotion(org):
        i = 1
        for promotion in org.promotions:
            print "-"*30
            print "# " + str(i) + " " + promotion.name + " %: " + str(promotion.perc)
            i += 1
        selected_prom = 0
        while selected_prom < 1 or selected_prom > i:
            selected_prom = int(raw_input("Select a promotion: "))
        prom_object = org.promotions[selected_prom-1]
        return prom_object

    @staticmethod
    def select_article(org):
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
        promotion = PromotionController.select_promotion(org)
        org.promotions.remove(promotion)

    @staticmethod
    def add_article(org):
        promotion = PromotionController.select_promotion(org)
        article = PromotionController.select_article(org)
        promotion.addArticle(article)
        print "Article successfully added"

    @staticmethod
    def remove_article(org):
        promotion = PromotionController.select_promotion(org)
        article = PromotionController.select_article(org)
        promotion.removeArticle(article)
        print "Article successfully removed"