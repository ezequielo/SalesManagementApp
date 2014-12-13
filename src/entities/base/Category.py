__author__ = 'ezequiel'

class Category:

    # Constructor

    def __init__(self, id_cat, cat_name, desc):
        self.cat_name = cat_name
        self.id_cat=id_cat
        self.desc = desc
        self.list_articulos = []
        self.commission = None
        self.org = None

    # Getter and setters

    def get_list_articulos(self):
        return self.list_articulos

    def set_list_articulos(self,list_articulos):
        self.list_articulos=list_articulos

    def get_cat_name(self):
        return self.cat_name

    def set_cat_name(self,cat_name):
        self.cat_name = cat_name

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc

    def get_id_cat(self):
        return self.id_cat

    def set_id_cat(self,id_cat):
        self.id_cat = id_cat

    def get_commission(self):
        return self.commission

    def set_commission(self,commission):
        self.commission = commission

    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org = org

    # Main methods

    def add_articulo(self, art):
        self.list_articulos.append(art)

    def remove_articulo(self, art):
        remove = False
        for article in self.list_articulos:
            if article.ean13 == art.ean13:
                remove = True
        if remove:
            self.list_articulos.remove(art)

    def __str__(self):
        return str(self.id_cat) + " - "+self.cat_name + " desc\n " + self.desc