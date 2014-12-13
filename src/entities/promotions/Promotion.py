__author__ = 'ezequiel'

class Promotion:

    # Constructor

    def __init__(self, name, perc, min):
        self.name = name
        self.perc = perc
        self.min = min
        self.list_articulos = []
        self.org = None
        self.promotion = None

    # Getters and setters

    def get_name(self):
        return self.name


    def set_name(self, name):
        self.name = name


    def get_perc(self):
        return self.perc

    def set_perc(self, perc):
        self.perc = perc


    def get_min(self):
        return self.min

    def set_min(self, min):
        self.min = min


    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org=org

    def get_promotion(self):
        return self.org

    def set_promotion(self, promotion):
        self.promotion=promotion


    def __str__(self):
        return self.name+ " - " +str(self.perc)
    # Main methods


    def addArticle(self, articulo):
        articulo.set_promotion(self)
        self.list_articulos.append(articulo)
        for art in self.list_articulos:
            if art.ean13 == articulo.ean13:
                self.list_articulos.append(articulo)
                return True
            else:
                return False


    def removeArticle(self, articulo):
        articulo.set_promotion(None)
        for art in self.list_articulos:
            if art.ean13 == articulo.ean13:
                self.list_articulos.remove(articulo)
                return True
            else:
                return False


