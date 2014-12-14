__author__ = 'ezequiel'


class Article:
    """

    Article class
    This class is responsible of modeling the articles of sale.

    """
    def __init__(self, cod, art_name, cost, list_price):
        """

        Init method
        Initializes an instance of Article class given the following parameters

        :param cod: code for generate ean13
        :param art_name: article name
        :param cost: article factory cost
        :param list_price: article sale cost

        """
        self.ean13 = None
        self.art_name = art_name
        self.cost = cost
        self.list_price = list_price
        self.commission = None
        self.promotion =  None
        # fill ean13 code
        self.set_ean13(cod)

    # Getters and setters
    def get_promotion(self):
        """

        Get promotion
        Get article promotion

        :return: article promotion or None if this have not promotion

        """
        return self.promotion

    def set_promotion(self, promotion):
        """

        Set promotion
        Allow to change actual article promotion

        :param promotion: new promotion

        """
        self.promotion = promotion

    def get_ean13(self):
        """

        Get ean13
        Get article identification with ean13 algorithm

        :return article identification

        """
        return self.ean13

    def set_ean13(self, cod):
        """

        Set ean13
        Allow to change actual cod

        :param cod: new code what permit generate ean13

        """
        cd = self.check_ean13(cod)
        ean13 = cod + str(cd)
        self.ean13 = ean13

    def get_art_name(self):
        """

        Get art name
        Get article name

        :return: article name

        """
        return self.art_name

    def set_art_name(self, art_name):
        """

        Set ean13
        Allow to change actual article name

        :param art_name: new article name

        """
        self.art_name = art_name

    def get_cost(self):
        """

        Get cost
        Get article factory cost

        :return: factory cost

        """
        return self.cost

    def set_cost(self, cost):
        """

        Set cost
        Allow to change article factory cost

        :param cost: factory cost

        """
        self.cost = cost

    def get_list_price(self):
        """

        Get list price
        Get article sale cost

        :return: sale cost

        """
        return self.list_price

    def set_list_price(self, list_price):
        """

        Set list price
        Allow to change actual article sale cost

        :param list_price: new sale cost

        """
        self.list_price = list_price

    def get_commission(self):
        """

        Get commission
        Returns the agent commission when this article is sold

        :return: Commission

        """
        return self.commission

    def set_commission(self, commission):
        """

        Set commission
        Allow to change actual the agent commission when this article is sold

        :param list_price: new the agent commission when this article is sold

        """
        self.commission = commission

    # Support methods
    def __str__(self):
        """

        Print article principal information

        :return: article principal information

        """
        return str(self.ean13) + " - " + self.art_name + " list price: " + str(self.list_price)

    def add_promotion(self, promotion):
        """

        Add promotion method
        Allows to add a new promotion to the organization agents list

        :param promotion: new promotion object

        """
        self.promotion.append(promotion)

    def remove_promotion(self, name):
        """

        Remove promotion method
        This method aims to remove a given promotion from the organization promotions list

        :param name: Promotion name to be removed

        """
        self.promotion.remove(name)

    def check_ean13(self, code):
        """

        Check_ean13
        Check article identification have a determinate patron

        :param code: Number for check article identification

        """
        checksum = 0
        for i, digit in enumerate(reversed(code)):
            checksum += int(digit) * 3 if (i % 2 == 0) else int(digit)
        return (10 - (checksum % 10)) % 10