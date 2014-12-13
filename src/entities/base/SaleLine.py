__author__ = 'ezequiel'


class SaleLine:
    # Constructor
    def __init__(self, uds, art):
        self.art = art
        self.uds = uds

    # Getter and setters
    def get_art(self):
        return self.art

    def set_art(self, article):
        self.art = article

    def get_uds(self):
        return self.uds

    def set_uds(self, uds):
        self.uds = uds

    # Main methods
    def get_subtotal(self):
        if self.get_art().get_promotion():
            promo = self.get_art().get_promotion()
            st = self.get_uds() * self.get_art().get_list_price() * promo.get_perc()
        else:
            st = self.get_uds() * self.get_art().get_list_price()
        return st

    def __str__(self):
        return str(self.art) + 'uds: ' + str(self.get_uds()) + ' subtotal: ' + str(self.get_subtotal())