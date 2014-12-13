__author__ = 'ezequiel'


class Promotion:
    # Constructor
    def __init__(self, name, percentage, minim):
        self.name = name
        self.percentage = percentage
        self.minim = minim
        self.article_list = []
        self.org = None
        self.promotion = None

    # Getters and setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_percentage(self):
        return self.percentage

    def set_percentage(self, percentage):
        self.percentage = percentage

    def get_minim(self):
        return self.minim

    def set_minim(self, minim):
        self.minim = minim

    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org = org

    def get_promotion(self):
        return self.org

    def set_promotion(self, promotion):
        self.promotion = promotion

    def __str__(self):
        return self.name + " - " + str(self.percentage)

    # Main methods
    def add_article(self, article):
        article.set_promotion(self)
        self.article_list.append(article)
        for art in self.article_list:
            if art.ean13 == article.ean13:
                self.article_list.append(article)
                return True
            else:
                return False

    def remove_article(self, article):
        article.set_promotion(None)
        for art in self.article_list:
            if art.ean13 == article.ean13:
                self.article_list.remove(article)
                return True
            else:
                return False