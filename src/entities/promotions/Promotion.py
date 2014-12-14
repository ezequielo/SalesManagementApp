__author__ = 'ezequiel'


class Promotion:
    # Constructor
    def __init__(self, name, percentage, minim):
        """

        Init method for Promotion of an article

        :param name: promotion name
        :param percentage: percentage reduction of article
        :param minim: minim reduction number

        """
        self.name = name
        self.percentage = percentage
        self.minim = minim
        self.article_list = []
        self.org = None
        self.promotion = None

    # Getters and setters
    def get_name(self):
        """
        Get promotion name

        :return: promotion name

        """
        return self.name

    def set_name(self, name):
        """

        Update actual promotion name

        :param name: New promotion name

        """
        self.name = name

    def get_percentage(self):
        """

        Get reduction percentage of article

        :return: reduction percentage

        """
        return self.percentage

    def set_percentage(self, percentage):
        """

        Update actual reduction percentage of article

        :param percentage: new reduction percentage

        """
        self.percentage = percentage

    def get_minim(self):
        """

        Get minim reduction percentage of article

        :return: minim reduction percentage

        """
        return self.minim

    def set_minim(self, minim):
        """

        Update actual minim reduction percentage of article

        :param minim: new minim reduction percentage

        """
        self.minim = minim

    def get_org(self):
        """

        Get cif of organization

        :return: cif

        """
        return self.org

    def set_org(self, org):
        """
        Update actual cif of organization

        :param org: new cif

        """
        self.org = org

    def get_promotion(self):
        """

        Get promotion instance

        :return: promotion

        """
        return self.org

    def set_promotion(self, promotion):
        """

        Update actual promotion instance

        :param promotion: new promotion

        """
        self.promotion = promotion

    def __str__(self):
        """

        Print promotion information

        :return: String instance

        """
        return self.name + " - " + str(self.percentage)

    # Main methods
    def add_article(self, article):
        """

        Add new article to promotion

        :param article:  new article
        :return: if it correct what the article is added

        """
        article.set_promotion(self)
        self.article_list.append(article)
        for art in self.article_list:
            if art.ean13 == article.ean13:
                self.article_list.append(article)
                return True
            else:
                return False

    def remove_article(self, article):
        """

        Remove an article to promotion

        :param article:  exist article
        :return: if it correct what the article is removed

        """
        article.set_promotion(None)
        for art in self.article_list:
            if art.ean13 == article.ean13:
                self.article_list.remove(article)
                return True
            else:
                return False