__author__ = 'ezequiel'


class Article:

    # Constructor
    def __init__(self, cod, art_name, cost, list_price):
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
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_ean13(self):
        return self.ean13

    def set_ean13(self, cod):
        cd = self.check_ean13(cod)
        ean13 = cod + str(cd)
        self.ean13 = ean13

    def get_art_name(self):
        return self.art_name

    def set_art_name(self, art_name):
        self.art_name = art_name

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_list_price(self):
        return self.list_price

    def set_list_price(self, list_price):
        self.list_price = list_price

    def get_commission(self):
        return self.commission

    def set_commission(self, commission):
        self.commission = commission

    # Support methods
    def __str__(self):
        return str(self.ean13) + " - " + self.art_name + " list price: " + str(self.list_price)

    def add_promotion(self, promotion):
        self.promotion.append(promotion)

    def remove_promotion(self, name):
        self.promotion.remove(name)

    def check_ean13(self, code):
        checksum = 0
        for i, digit in enumerate(reversed(code)):
            checksum += int(digit) * 3 if (i % 2 == 0) else int(digit)
        return (10 - (checksum % 10)) % 10