__author__ = 'ezequiel'


class Category:
    # Constructor
    def __init__(self, id_cat, cat_name, desc):
        self.cat_name = cat_name
        self.id_cat = id_cat
        self.desc = desc
        self.article_list = []
        self.commission = None
        self.org = None

    # Getter and setters

    def get_article_list(self):
        return self.article_list

    def set_article_list(self, article_list):
        self.article_list = article_list

    def get_cat_name(self):
        return self.cat_name

    def set_cat_name(self, cat_name):
        self.cat_name = cat_name

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc

    def get_id_cat(self):
        return self.id_cat

    def set_id_cat(self, id_cat):
        self.id_cat = id_cat

    def get_commission(self):
        return self.commission

    def set_commission(self, commission):
        self.commission = commission

    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org = org

    # Main methods
    def add_article(self, art):
        self.article_list.append(art)

    def remove_article(self, art):
        remove = False
        for article in self.article_list:
            if article.ean13 == art.ean13:
                remove = True
        if remove:
            self.article_list.remove(art)

    def __str__(self):
        return str(self.id_cat) + " - "+self.cat_name + " desc\n " + self.desc