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
        self.art=article


    def get_uds(self):
        return self.uds

    def set_uds(self, uds):
        self.uds=uds


    # Main methods

    def getSubtotal(self):
        st = 0.0
        if self.get_art().get_promotion():
            promo = self.get_art().get_promotion()
            st = self.get_uds()*self.get_art().get_listprice()*promo.get_perc()
        else:
            st = self.get_uds()*self.get_art().get_listprice()
        return st



    def __str__(self):
        return str(self.art)+'uds: '+str(self.get_uds())+ ' subtotal: '+str(self.getSubtotal())